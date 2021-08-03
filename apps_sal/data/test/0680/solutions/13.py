a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
s = [a[:], b[:], c[:]]
a, b, c = sorted([a, b, c])

if c[1] < b[1]:
    c[1], b[1] = b[1], c[1]

if b[1] < a[1]:
    b[1], a[1] = a[1], b[1]

if c[1] < b[1]:
    b[1], c[1] = c[1], b[1]


def man_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + 1


dist = man_dist(a, b) + man_dist(b, c) - 1
s.sort()
a = set()

for i in range(s[0][0], s[1][0] + 1):
    a.add((i, s[0][1]))


if s[0][1] < s[1][1]:
    for i in range(s[0][1], s[1][1] + 1):
        a.add((s[1][0], i))
else:
    for i in range(s[1][1], s[0][1] + 1):
        a.add((s[1][0], i))

x = man_dist(s[1], s[2])
y = man_dist((s[1][0], s[0][1]), s[2])
z = man_dist((s[1][0], s[2][1]), s[2])

if s[2][1] in range(min(s[0][1], s[1][1]), max(s[0][1], s[1][1])):
    int_point = (s[1][0], s[2][1])
elif (y > x and y > z):
    int_point = (s[1][0], s[1][1])
else:
    int_point = (s[1][0], s[0][1])

for i in range(int_point[0], s[2][0] + 1):
    a.add((i, int_point[1]))

if int_point[1] < s[2][1] + 1:
    for i in range(int_point[1], s[2][1] + 1):
        a.add((s[2][0], i))
else:
    for i in range(s[2][1], int_point[1] + 1):
        a.add((s[2][0], i))

print(dist)
for i in a:
    print(*i)
