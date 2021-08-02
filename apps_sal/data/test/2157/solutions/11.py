import sys
n, q = list(map(int, sys.stdin.readline().split()))
l1 = [0] + list(map(int, sys.stdin.readline().split()))
l1.sort()
b = []
for i in range(0, n + 2):
    b.append(0)
for jj in range(0, q):
    l, r = list(map(int, sys.stdin.readline().split()))
    b[l] += 1
    b[r + 1] -= 1
for i in range(2, n + 1):
    b[i] += b[i - 1]
b.sort()
sum1 = 0
k = len(b)
k -= 1
kk = n
for i in range(1, n + 1):
    sum1 += (b[k] * l1[kk])
    k -= 1
    kk -= 1
print(sum1)
