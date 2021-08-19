n = int(input())
a = []
b = []
for i in range(n):
    (l, r) = [int(_) for _ in input().strip().split()]
    a.append(l)
    b.append(r)
a.sort()
b.sort()
print(n + sum([max(a[_], b[_]) for _ in range(n)]))
