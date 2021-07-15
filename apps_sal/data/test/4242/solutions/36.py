A, B, K = (int(i) for i in input().split())
m = []
for i in range(100, 0, -1):
    if (A % i == 0) and (B % i == 0):
        m.append(i)
print(m[K - 1])
