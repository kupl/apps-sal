def f(n):
    if n == 0:
        return 1
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans


n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a = sorted(a)
ans = f(n - m) // f(a[0] - 1)
for i in range(1, m):
    ans //= f(a[i] - a[i - 1] - 1)
    if a[i] - a[i - 1] != 1:
        ans *= 2 ** (a[i] - a[i - 1] - 2)
ans //= f(n - a[m - 1])
print(ans % 1000000007)
