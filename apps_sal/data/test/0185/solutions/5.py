ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

n, k = mi()
if k - 1 > n - k:
    k = n - k + 1

ans = n + k - 1 + 1 + n + n - 1
print(ans)
