N = int(input())
S = input()


for s in ['SS', 'SW', 'WS', 'WW']:
    ss = s
    jdg = False
    for i in range(1, N):
        if S[i] == 'o':
            if ss[i] == 'S':
                ss += ss[i - 1]
            else:
                if ss[i - 1] == 'W': ss += 'S'
                else: ss += 'W'
        else:
            if ss[i] == 'S':
                if ss[i - 1] == 'W': ss += 'S'
                else: ss += 'W'
            else:
                ss += ss[i - 1]
    if ss[N] == ss[0]:
        if S[0] == 'o':
            if (ss[0] == 'S' and ss[N - 1] == ss[1]) or (ss[0] == 'W' and ss[N - 1] != ss[1]):
                jdg = True
                break
        else:
            if (ss[0] == 'S' and ss[N - 1] != ss[1]) or (ss[0] == 'W' and ss[N - 1] == ss[1]):
                jdg = True
                break
print((ss[:-1] if jdg else -1))
