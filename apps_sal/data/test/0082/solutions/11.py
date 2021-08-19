(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
while 2 * (sum(a) + ans * k) < (n + ans) * (2 * k - 1):
    ans += 1
print(ans)
