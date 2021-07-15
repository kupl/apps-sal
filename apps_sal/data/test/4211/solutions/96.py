n = int(input())
b = [int(s) for s in input().split()]
b.append(b[n - 2])
a = [0] * n
a[0] = b[0]
for i in range(1, n):
    a[i] = min(b[i - 1], b[i])
print(sum(a))
