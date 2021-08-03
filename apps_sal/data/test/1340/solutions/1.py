n = int(input())
a = [int(x) for x in input().split()]

d = {}
for i in range(1, 21):
    for j in range(1, 21):
        d[(i, j)] = 0
cv = [0 for i in range(21)]

for j in a:
    for i in range(1, 21):
        d[(i, j)] += cv[i]
    cv[j] += 1

s = 0
for i in range(1, 21):
    for j in range(i + 1, 21):
        s += min(d[(i, j)], d[(j, i)])
print(s)
