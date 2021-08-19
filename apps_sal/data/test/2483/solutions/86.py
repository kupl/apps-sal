(n, C) = map(int, input().split())
chs = [[] for i in range(31)]
for i in range(n):
    (s, t, c) = map(int, input().split())
    chs[c].append((s, t))
for q in range(len(chs)):
    ch = chs[q][:]
    ch.sort()
    new = []
    if len(ch) <= 1:
        continue
    else:
        now = ch[0]
        for i in range(1, len(ch)):
            if now[1] == ch[i][0]:
                now = (now[0], ch[i][1])
            else:
                new.append(now)
                now = ch[i]
        new.append(now)
        chs[q] = new[:]
tim = [0 for i in range(200002)]
for ch in chs:
    for pro in ch:
        tim[pro[0] * 2 - 1] += 1
        tim[pro[1] * 2] -= 1
cnt = 0
ans = 0
for i in range(len(tim)):
    cnt += tim[i]
    ans = max(ans, cnt)
print(ans)
