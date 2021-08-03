n = int(input())
a = [int(i) for i in input().split()]
a.sort()
r = []
for i in range(0, len(a) - 1):
    r.append(abs(a[i] - a[i + 1]))
r.sort()
print(r[0], r.count(r[0]))
