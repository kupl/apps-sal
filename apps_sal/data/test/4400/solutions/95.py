S = input()
n_S = len(S)
state_r = 0
ma = 0

for i in range(n_S):
    if S[i] == 'R':
        state_r += 1
    else:
        state_r = 0
    ma = max(ma, state_r)

print(ma)

