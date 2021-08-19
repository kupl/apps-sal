(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = [list(map(int, input().split())) for i in range(m)]
gl_ans = -1
gl_mas = []
for num_i in range(n):
    ma = -10000000.0
    ans_m = []
    o = []
    for i in range(m):
        if b[i][0] - 1 > num_i or b[i][1] - 1 < num_i:
            o.append([b[i][0] - 1, -1])
            o.append([b[i][1], 0])
            ans_m.append(i + 1)
    for i in range(n):
        o.append([i, 1])
    o.sort()
    cnt = 0
    mi = 10000000.0
    for u in range(len(o)):
        if o[u][1] == -1:
            cnt -= 1
        elif o[u][1] == 0:
            cnt += 1
        elif a[o[u][0]] + cnt < mi:
            mi = a[o[u][0]] + cnt
    ma = a[num_i]
    if ma - mi > gl_ans:
        gl_ans = ma - mi
        gl_mas = ans_m
print(gl_ans)
print(len(gl_mas))
print(*gl_mas)
