def ii(): return int(input())
def mi(): return list(map(int, input().split()))
def li(): return list(mi())


n, m, k = mi()
b = li()
if k >= n:
    ans = n
else:
    d = sorted((b[i + 1] - b[i], i) for i in range(n - 1))[::-1]
    s = {i for x, i in d[:k - 1]}
    ans = n
    for i in range(n - 1):
        if i not in s:
            ans += b[i + 1] - b[i] - 1
print(ans)
