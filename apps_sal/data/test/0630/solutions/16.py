def s(x, y):
    nonlocal k, n
    if x - y - 1 >= 2 * k:
        return k + 1 + min(k, n - x - 1)
    elif x - y - 1 >= k:
        return min(n - x - 1, k) + x - y - k
    else:
        return min(n - 1, x + k) - min(n - 1, y + k)


def search(i):
    nonlocal a, n, k, ans
    if a[i] == -1:
        ans[i] = min(k, i) + min(k, n - i - 1) + 1
        return min(k, i) + min(k, n - i - 1) + 1
    else:
        if ans[i] == 0:
            ans[i] = search(a[i]) + s(i, a[i])
            return search(a[i]) + s(i, a[i])
        else:
            return ans[i]


n, k = input().split()
n = int(n)
k = int(k)
ans = []
a = input().split()
for i in range(n):
    a[i] = int(a[i]) - 1
    ans.append(0)
for i in range(n):
    if ans[i] == 0:
        ans[i] = search(i)
for i in range(len(ans)):
    print(ans[i], end=' ')
