# input

n, x = list(map(int, input().split()))
m = []
for i in range(n):
    m.append([int(x) for x in input().split()])


# variables
r = 1
t = 0


# main

for i in range(n):
    t += (m[i][0] - r) % x + m[i][1] - m[i][0] + 1
    r = (m[i][1] + 1) % x


# output
print(t)
