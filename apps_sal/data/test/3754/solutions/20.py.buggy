MOD = 998244353
n = int(input())
dlst = list(map(int, input().split()))
ans = 1
total = sum(dlst)
if total < 2 * (n - 1):
    print(0)
    return
for d in dlst:
    ans *= d
    ans %= MOD
total -= n
for _ in range(n - 2):
    ans *= total
    ans %= MOD
    total -= 1
print(ans)
