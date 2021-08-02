n, m = map(int, input().split())
a = [input().split()for _ in range(m)]
c = [0] * n
w = [0] * n
for i in range(m):
    if c[int(a[i][0]) - 1] == 0:
        if a[i][1] == "AC":
            c[int(a[i][0]) - 1] += 1
        else:
            w[int(a[i][0]) - 1] += 1
    else:
        pass
for i in range(n):
    if c[i] == 0:
        w[i] = 0
    else:
        pass
print(sum(c), sum(w))
