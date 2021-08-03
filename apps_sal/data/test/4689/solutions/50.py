k, n = list(map(int, input().split()))

a = list(map(int, input().split()))
a.sort()
a.append(k + a[0])

b = [0] * (n)
for i in range(n):
    b[i] = a[i + 1] - a[i]

print((k - max(b)))
