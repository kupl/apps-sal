n = int(input())
a = []
for i in range(n):
    s, p = input().split()
    p = int(p)
    a.append([s, -p, i])
a.sort()

for i in a:
    print((i[2] + 1))
