def lowbit(index):
    return index & (-index)


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


n, t = list(map(int, input().split()))
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
    cur = (query(size) - query(index))
    res += cur
    update(d[v])
print(res)


'''

n, t = list(map(int, input().split()))
a = list(map(int, input().split()))

summ = [0]
cur = 0
for i in range(n):
    cur += a[i]
    summ.append(cur)


def merge(l, mid, r):
    i, j = l, mid + 1
    ans = 0
    while i <= mid and j <= r:
        if summ[i] + t > summ[j]:
            ans += (mid + 1 - i)
            j += 1
        else:
            i += 1

    tmp = []
    i, j = l, mid + 1
    while i <= mid and j <= r:
        if summ[i] <= summ[j]:
            tmp.append(summ[i])
            i += 1
        else:
            tmp.append(summ[j])
            j += 1
    if i <= mid:
        tmp.extend(summ[i:mid + 1])
    if j <= r:
        tmp.extend(summ[j:r+1])
    for i in range(l, r + 1):
        summ[i] = tmp[i - l]

    return ans



def helper(l, r):
    if l == r:
        return 0
    mid = (l + r) // 2
    ans1 = helper(l, mid)
    ans2 = helper(mid + 1, r)
    ans3 = merge(l, mid, r)
    return ans1 + ans2 + ans3

res = helper(0, n)
print(res)
'''

'''
5 4
5 -1 3 4 -1

Output

5

Input

3 0
-1 2 -3

Output

4

Input

4 -1
-2 1 -2 3

Output

3
'''
