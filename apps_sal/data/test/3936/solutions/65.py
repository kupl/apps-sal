MOD = 1000000007
N = int(input())
S1 = input()
S2 = input()
ans = 1
idx = 0
if S1[idx] == S2[idx]:
    ans *= 3
    idx += 1
else:
    ans *= 6
    idx += 2
while idx < N:
    if S1[idx] == S2[idx]:
        if S1[idx - 1] == S2[idx - 1]:
            ans *= 2
        idx += 1
    else:
        if S1[idx - 1] == S2[idx - 1]:
            ans *= 2
        else:
            ans *= 3
        idx += 2
ans %= MOD
print(ans)
