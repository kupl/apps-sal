N = int(input())
s = list(input())
s = s * 2
q = [[True, True], [True, False], [False, True], [False, False]]
p = []
ans = []
for k in range(4):
    p = q[k]
    for i in range(N * 2 - 2):
        if p[i + 1]:
            if s[i + 1] == "o":
                p.append(p[i])
            else:
                p.append(not p[i])
        else:
            if s[i + 1] == "o":
                p.append(not p[i])
            else:
                p.append(p[i])
    if p[0:N - 1] == p[N:N * 2 - 1]:
        for i in range(N):
            if p[i]:
                ans.append("S")
            else:
                ans.append("W")
        print("".join(ans))
        break
    if k == 3:
        print(-1)
