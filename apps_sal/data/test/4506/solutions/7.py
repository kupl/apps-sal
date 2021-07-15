def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
MOD = 998244353

n = getN()
anums = getList()
bnums = getList()
anums = [a * (i+1) * (n-i) for i, a in enumerate(anums)]
anums.sort()
bnums.sort(reverse=True)
ans = 0
for a, b in zip(anums, bnums):
    ans += a * b
    ans = ans % MOD

print(ans)
