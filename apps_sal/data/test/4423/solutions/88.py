n = int(input())
l = []
for i in range(n):
    (city, point) = input().split()
    point = int(point)
    l.append((city, -point, i + 1))
for i in sorted(l):
    print(i[2])
