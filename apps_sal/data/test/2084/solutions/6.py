n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a.sort()
s = 0

for i in range(k):
    s += a[i]

print(s)

