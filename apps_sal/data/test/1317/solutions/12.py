n, m = map(int, input().split())
f = lambda r: ((n - r)//m) - ((m - r)//m) + 1
res = 0
for i in range(m):
    for j in range(i, m):
        if ((i**2) + (j**2)) % m == 0:
            # print(i, j, f(i), f(j))
            res += f(i) * f(j) * (2 if i != j else 1) 
print(res)
