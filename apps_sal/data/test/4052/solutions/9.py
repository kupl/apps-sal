n = int(input())

s = input()
t = input()

if sorted(s) != sorted(t):
    print(-1)
else:
    moves = []
    s = list(s)
    t = list(t)
    for ind_t, val_t in enumerate(t):
        i = ind_t + s[ind_t:].index(val_t)
        for j in range(i - 1, ind_t - 1, -1):
            moves.append(j + 1)
            s[j], s[j + 1] = s[j + 1], s[j]
    print(len(moves))
    print(" ".join(str(x) for x in moves))
