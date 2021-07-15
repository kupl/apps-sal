N, K = list(map(int, input().split()))
S = input()
RL = 0
for i in range(N - 1):
    if S[i] == 'R' and S[i + 1] == 'L':
        RL += 1
egde = (S[0] == 'L') + (S[-1] == 'R')
if K >= RL:
    K -= RL
    RL = 0
    if K > 0:
        egde = max(1, egde - K)
else:
    RL -= K
print((N  - 2 * RL - egde))

