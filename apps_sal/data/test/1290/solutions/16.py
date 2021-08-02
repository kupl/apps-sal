n, m = (int(x) for x in input().split())

a = [int(x) for x in input().split()]

b = [0] * n
for i in range(m):
    b[a[i] - 1] += 1
print(min(b))
