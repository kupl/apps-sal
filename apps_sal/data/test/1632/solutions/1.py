import sys

# sys.stdin = open("ivo.in")

n = int(sys.stdin.readline())

a = [int(s) for s in sys.stdin.readline().split()]

a.sort()

diffs1 = []

for i in range(5000):
    diffs1.append(0)

for i in range(n):
    for j in range(i + 1, n):
        diffs1[a[j] - a[i]] += 1

# for i in range(1, n):
#    diffs1[i] += diffs1[i - 1]

diffs2 = []
for i in range(10000):
    diffs2.append(0)

for i in range(len(diffs1)):
    for j in range(i, len(diffs1)):
        if i == j:
            diffs2[i + j] += diffs1[i] * diffs1[j]
        else:
            diffs2[i + j] += 2 * diffs1[i] * diffs1[j]

for i in range(1, len(diffs2)):
    diffs2[i] += diffs2[i - 1]


good = 0
for u in range(n - 1, 0, -1):
    for t in range(u - 1, -1, -1):
        good += diffs2[a[u] - a[t] - 1]

all = (n * (n - 1)) // 2
all = all * all * all

print(float(good) / float(all))
