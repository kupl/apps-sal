n = int(input())
c = []
for i in range(n):
    (a, b) = input().split()
    c.append([i + 1, a, -int(b)])
c = sorted(c, key=lambda x: (x[1], x[2]))
for i in c:
    print(i[0])
