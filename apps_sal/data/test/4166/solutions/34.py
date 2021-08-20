(n, m) = list(map(int, input().split()))
ng = [tuple(map(int, input().split())) for _ in range(m)]
for i in range(1000):
    i = str(i)
    if len(i) != n:
        continue
    for g in ng:
        if i[g[0] - 1] != str(g[1]):
            break
    else:
        print(i)
        break
else:
    print(-1)
