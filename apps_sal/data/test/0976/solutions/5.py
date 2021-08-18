
n, x = list(map(int, input().split()))
m = []
for i in range(n):
    m.append([int(x) for x in input().split()])


r = 1
t = 0


for i in range(n):
    t += (m[i][0] - r) % x + m[i][1] - m[i][0] + 1
    r = (m[i][1] + 1) % x


print(t)
