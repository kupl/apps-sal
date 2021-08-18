import sys
MOD = 1000000007

N = int(input())
S1 = input()
S2 = input()

pattern = []
pos = 0

if N == 1:
    print(3)
    return

while True:
    if S1[pos] != S1[pos + 1]:
        pattern.append(0)
        pos += 1
    else:
        pattern.append(1)
        pos += 2
    if pos == N - 1:
        pattern.append(0)
        break
    elif pos == N:
        break

if pattern[0] == 0:
    ans = 3
    now = 0
else:
    ans = 6
    now = 1

for i in range(1, len(pattern)):
    if pattern[i] == 0:
        if now == 0:
            ans *= 2
            ans = ans % MOD
        else:
            ans *= 1
            ans = ans % MOD
        now = 0
    else:
        if now == 0:
            ans *= 2
            ans = ans % MOD
        else:
            ans *= 3
            ans = ans % MOD
        now = 1

print(ans)
