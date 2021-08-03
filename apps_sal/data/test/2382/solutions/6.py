N = int(input())
N2 = 1 << N

S = sorted([int(x) for x in input().split()])

s = []
s.append(S[-1])
S[-1] = -1

flag = True
for i in range(N):
    p = sorted([x for x in s])

    Si = N2 - 1
    while len(p) > 0 and Si >= 0:
        if S[Si] == -1:
            Si -= 1
            continue

        if S[Si] < p[-1]:
            s.append(S[Si])
            del p[-1]
            S[Si] = -1

        Si -= 1

    if len(p) > 0:
        flag = False

print('Yes' if flag else 'No')
