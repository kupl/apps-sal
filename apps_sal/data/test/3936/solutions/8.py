MOD = 10 ** 9 + 7
N = int(input())
S1 = input()
S2 = input()

ans = 1
i = 0
if S1[i] == S2[i]:
    ans *= 3
    prev = True
    i += 1
else:
    ans *= 6
    prev = False
    i += 2

while i < N:
    now = (S1[i] == S2[i])
    if now:
        if prev:
            ans *= 2
            ans %= MOD
        else:
            pass
        i += 1
    else:
        if prev:
            ans *= 2
            ans %= MOD
        else:
            ans *= 3
            ans %= MOD
        i += 2
    prev = now
print(ans)
