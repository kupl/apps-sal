MODINT = 1000000007
n, k = map(int, input().split())
prod = [0] * (n + 1)

for i in range(1, n + 1):
    prod[i] = prod[i - 1] + i
# print(prod)
ans = 0
for s in range(k - 1, n + 1):
    L = prod[s]
    R = prod[n] - prod[n - s] + (n - s)
    # print(L,R)
    ans += R - L + 1
    ans %= MODINT
print(ans)
