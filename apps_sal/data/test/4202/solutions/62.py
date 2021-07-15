MOD = 2019

l, r = map(int, input().split())
if r - l >= 2019:
    print(0)
    return
lst = []
for num in range(l, r + 1):
    lst.append(num % MOD)
ans = 2020
ll = len(lst)
for i in range(ll):
    for j in range(i + 1, ll):
        tmp = (lst[i] * lst[j]) % MOD
        ans = min(ans, tmp)
print(ans)
