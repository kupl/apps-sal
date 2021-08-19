S = input() + 'R'
L = len(S)
RL = 0
(l, r, f) = (0, 0, 0)
a = [0] * (L - 1)
for i in range(1, L):
    if f:
        r += 1
    else:
        l += 1
    if S[i - 1:i + 1] == 'LR':
        a[RL - 1] = r // 2 + (l + 1) // 2
        a[RL] = (r + 1) // 2 + l // 2
        (l, r, f) = (0, 0, 0)
    if S[i - 1:i + 1] == 'RL':
        (RL, f) = (i, 1)
print(' '.join(map(str, a)))
