n, k = list(map(int, input().split()))
d = list(zip(list(map(int, input().split())), list(range(0, n))))
d = sorted(d)

last = 0
du = [0] * n
fa = [0] * n
flag = 1
for j in range(1, n):
    while last < j and (du[last] == k or d[last][0] + 1 != d[j][0]):
        last += 1
    if last == j or d[0][0] != 0:
        print(-1)
        break
    fa[j] = last
    du[j] += 1
    du[last] += 1
else:
    print(n - 1)
    for j in range(1, n):
        print(d[fa[j]][1] + 1, d[j][1] + 1)
