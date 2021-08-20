n = int(input())
p = list(map(int, input().split()))
p = sorted(list(enumerate(p)), key=lambda x: -x[1])
a = [[]]
for i in range(n):
    a.append(sorted(a[-1] + [p[i]], key=lambda x: x[0]))
m = int(input())
for _ in range(m):
    (x, y) = list(map(int, input().split()))
    print(a[x][y - 1][1])
