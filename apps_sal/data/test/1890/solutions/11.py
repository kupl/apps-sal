MOD = 1000000007
data = input().strip()
k = int(input())
ans = 0
alc = 1
for i, d in enumerate(data):
    if d == "0" or d == "5":
        ans += alc
    alc *= 2
    alc %= MOD
print(ans * (pow(alc, k, MOD) - 1) * pow(alc - 1, MOD - 2, MOD) % MOD)


