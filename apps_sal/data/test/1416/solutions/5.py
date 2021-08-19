#n = int(input())
n, w = [int(c) for c in input().split()]
a = [int(c) for c in input().split()]
a.sort()

maxgirl = w / (3 * n)

for i in range(n):
    if a[i] < maxgirl:
        maxgirl = a[i]
for i in range(n, 2 * n):
    if a[i] < 2 * maxgirl:
        maxgirl = a[i] / 2

print(maxgirl * 3 * n)
