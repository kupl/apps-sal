(n, k) = [int(x) for x in input().split()]
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
a.sort()
c = 0
while k > 0:
    k -= a[c][1]
    c += 1
print(a[c - 1][0])
