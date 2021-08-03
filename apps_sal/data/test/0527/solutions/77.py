from collections import defaultdict
S = input()
T = input()


nx = [defaultdict(lambda: -1) for i in range(len(S) + 1)]
lastpos = defaultdict(lambda: 0)

SS = S + S
for i, c in enumerate(SS[::-1]):
    i = len(SS) - 1 - i
    if i < len(S):
        for k, v in lastpos.items():
            nx[i + 1][k] = v - i
    lastpos[c] = i
for k, v in lastpos.items():
    nx[0][k] = v + 1

ans = 0
for c in T:
    if nx[ans % len(S)][c] == -1:
        print(-1)
        return
    ans += nx[ans % len(S)][c]
print(ans)
