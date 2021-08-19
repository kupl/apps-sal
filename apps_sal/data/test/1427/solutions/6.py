from collections import defaultdict
MOD = 10 ** 9 + 7
n = int(input())
alst = list(map(int, input().split()))
dd = defaultdict(int)
ans = 0
for a in alst:
    ans += pow(a, MOD - 2, MOD)
    ans %= MOD
    num = a
    for i in range(2, int(a ** 0.5) + 1):
        cnt = 0
        while num % i == 0:
            num //= i
            cnt += 1
        if cnt > 0:
            dd[i] = max(dd[i], cnt)
    if num != 1:
        dd[num] = max(dd[num], 1)
for (key, value) in list(dd.items()):
    ans *= pow(key, value, MOD)
    ans %= MOD
print(ans)
