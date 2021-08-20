n = int(input())
all_h_or_u = []
for i in range(n):
    x = int(input())
    h_or_u = []
    for j in range(x):
        h_or_u.append(list(map(int, input().split())))
    for k in range(x):
        h_or_u[k][0] -= 1
    all_h_or_u.append(h_or_u)
all_t_or_f = []
for a in range(2 ** n):
    t_or_f = []
    for b in range(len(bin(2 ** n)) - 3):
        if a >> b & 1:
            t_or_f.append(1)
        else:
            t_or_f.append(0)
    all_t_or_f.append(t_or_f)
max_cnt = 0
for c in all_t_or_f:
    cnt = 0
    for d in range(n):
        if c[d] == 1:
            for e in all_h_or_u[d]:
                if c[e[0]] != e[1]:
                    cnt += 1
    if cnt == 0:
        max_cnt = max(max_cnt, sum(c))
print(max_cnt)
