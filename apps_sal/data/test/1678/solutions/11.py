def lowbit(index):
    return index & -index


def update(index, delta=1):
    while index <= size:
        tree[index] += delta
        index += lowbit(index)


def query(index):
    res = 0
    while index > 0:
        res += tree[index]
        index -= lowbit(index)
    return res


(n, t) = list(map(int, input().split()))
a = list(map(int, input().split()))
summ_raw = [0]
summ_minus = []
cur = 0
for i in range(n):
    cur += a[i]
    summ_raw.append(cur)
    summ_minus.append(cur - t)
summ = sorted(list(set(summ_raw + summ_minus)))
size = len(summ)
d = {}
for i in range(size):
    d[summ[i]] = i + 1
tree = [0] * (size + 1)
update(d[0])
res = 0
for i in range(1, n + 1):
    v = summ_raw[i]
    index = d[v - t]
    cur = query(size) - query(index)
    res += cur
    update(d[v])
print(res)
'\n# divide and conquer, two pointers\n\nn, t = list(map(int, input().split()))\na = list(map(int, input().split()))\n\nsumm = [0]\ncur = 0\nfor i in range(n):\n    cur += a[i]\n    summ.append(cur)\n\n\ndef merge(l, mid, r):\n    i, j = l, mid + 1\n    ans = 0\n    while i <= mid and j <= r:\n        if summ[i] + t > summ[j]:\n            ans += (mid + 1 - i)\n            j += 1\n        else:\n            i += 1\n\n    tmp = []\n    i, j = l, mid + 1\n    while i <= mid and j <= r:\n        if summ[i] <= summ[j]:\n            tmp.append(summ[i])\n            i += 1\n        else:\n            tmp.append(summ[j])\n            j += 1\n    if i <= mid:\n        tmp.extend(summ[i:mid + 1])\n    if j <= r:\n        tmp.extend(summ[j:r+1])\n    for i in range(l, r + 1):\n        summ[i] = tmp[i - l]\n\n    return ans\n\n\n\ndef helper(l, r):\n    if l == r:\n        return 0\n    mid = (l + r) // 2\n    ans1 = helper(l, mid)\n    ans2 = helper(mid + 1, r)\n    ans3 = merge(l, mid, r)\n    #print(ans1, ans2, ans3)\n    return ans1 + ans2 + ans3\n\nres = helper(0, n)\nprint(res)\n'
'\n5 4\n5 -1 3 4 -1\n\nOutput\n\n5\n\nInput\n\n3 0\n-1 2 -3\n\nOutput\n\n4\n\nInput\n\n4 -1\n-2 1 -2 3\n\nOutput\n\n3\n'
