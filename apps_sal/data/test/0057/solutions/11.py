n = int(input())
v = []
for i in range(n):
    v.append(list(map(int, input().split())))
ans = False
for (xi, yi) in v:
    if ans:
        break
    for (xj, yj) in v:
        if xi != xj and yi != yj:
            print(abs(xi - xj) * abs(yi - yj))
            ans = True
            break
if not ans:
    print(-1)
