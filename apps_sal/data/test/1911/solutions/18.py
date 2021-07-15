import sys

n, k = list(map(int, sys.stdin.readline().strip().split()))
a = list(map(int, sys.stdin.readline().strip().split()))
b = [0] * (n-1)
for i in range (0, n-1):
    b[i] = a[i+1]-a[i]
b.sort(reverse = True)
print(a[n-1]-a[0]-sum(b[0:k-1]))

