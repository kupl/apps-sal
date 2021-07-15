from collections import Counter
from itertools import permutations

n, c = map(int, input().split())

a = []
b = []

for _ in range(c):
    array = list(map(int, input().split()))
    a.append(array)

for _ in range(n):
    array = list(map(int, input().split()))
    b.append(array)


group1 = []
group2 = []
group3 = []

for i in range(n):
    for j in range(n):
        if (i + j) % 3 == 0:
            group1.append(b[i][j])
        elif (i + j) % 3 == 1:
            group2.append(b[i][j])
        else:
            group3.append(b[i][j])

g1 = Counter(group1)
g2 = Counter(group2)
g3 = Counter(group3)

sum1 = []
sum2 = []
sum3 = []


def cal(l, output):
    for i in range(c):
        s = 0
        for j in l.items():
            s += a[j[0]-1][i-1] * j[1]
        output.append(s)


li = [g1, g2, g3]
li2 = [sum1, sum2, sum3]

for i in range(3):
    cal(li[i], li2[i])

cc = list(range(c))

min_sum = 10**10
for i, j, k in permutations(cc, 3):
    sum = sum1[i] + sum2[j] + sum3[k]
    if sum < min_sum:
        min_sum = sum

print(min_sum)
