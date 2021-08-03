n = int(input())
b = [int(x) for x in input().split()]
a = [0] * n
a[0] = b[0]
a[n - 1] = b[n - 2]
for i in range(1, n - 1):
    s = min(b[i], b[i - 1])
    a.append(s)

print(sum(a))
