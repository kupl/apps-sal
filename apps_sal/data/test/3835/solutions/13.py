n = int(input())

t = [list(map(int, input().split())) for i in range(n)]

b = int((t[0][1] * t[1][2] / t[0][2]) ** 0.5)
a = []
a.append(t[0][1] // b)
a.append(b)

for i in range(2, n):
    a.append(t[i][1] // b)

print(*a)

