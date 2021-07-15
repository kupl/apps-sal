MOD = 10**9 + 7
N = int(input())
S1 = input().rstrip()
S2 = input().rstrip()
L = len(S1)

if L==1:
    print((3))
    return

if S1[0] == S1[1]:
    dp = 6
    start = 2
    state = 0
else:
    dp = 3
    start = 1
    state = 1

i = start
while i<L-1:
    if S1[i] == S1[i+1]:
        if state == 0:
            dp *= 3
            dp %= MOD
        else:
            dp *= 2
            dp %= MOD
        state = 0
        i += 2
    else:
        if state == 1:
            dp *= 2
            dp %= MOD
        state = 1
        i += 1
if state == 1:
    dp *= 2
    dp %= MOD
print(dp)

