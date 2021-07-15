n, a, b, c = list(map(int, input().split()))
res = 10000000000
for i in range(10):
    for j in range(10):
        for k in range(10):
            if (n + i + j*2 + k*3)%4 == 0:
                res = min(res, i*a + j*b + k*c)

print(res)

