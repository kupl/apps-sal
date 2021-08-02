import sys

line = sys.stdin.readline().strip().split()
n = int(line[0])
c = int(line[1])
a = list(map(int, sys.stdin.readline().strip().split()))
cright = [0] * (n + 1)
maxfreq = [0] * (5 * 10 ** 5 + 1)

for i in range(0, n):
    if a[n - 1 - i] == c:
        cright[n - 1 - i] = cright[n - i] + 1
    else:
        cright[n - 1 - i] = cright[n - i]

result = cright[0]
cleft = 0

for i in range(0, n):
    if a[i] != c:
        maxfreq[a[i]] = max([maxfreq[a[i]], cleft]) + 1
    else:
        cleft = cleft + 1
    if maxfreq[a[i]] + cright[i + 1] > result:
        result = maxfreq[a[i]] + cright[i + 1]

print(result)
