[n, k] = [int(x) for x in input().split(' ')]
A = [int(x) for x in input().split(' ')]
m = -1
valm = 10 ** 10
for i in range(k):
    temp = sum([A[(k * j + i) % n] for j in range(n // k)])
    if temp < valm:
        valm = temp
        m = i
print(m + 1)
