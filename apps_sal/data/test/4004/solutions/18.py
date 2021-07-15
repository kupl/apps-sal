n = int(input())
u = list(map(int, input().split()))
u.sort()
p = [u[0]]
for i in range(1, n):
    if u[i] != u[i - 1]:
        p.append(u[i])
        if len(p) == 4:
            print(-1)
            return
if len(p) == 1:
    print(0)
elif len(p) == 2:
    if abs(p[1] - p[0]) % 2 == 0:
        print(abs(p[1] - p[0]) // 2)
    else:
        print(abs(p[1] - p[0]))
else:
    if p[1] - p[0] == p[2] - p[1]:
        print(p[2] - p[1])
    else:
        print(-1)

