import sys
input = sys.stdin.readline
n = int(input())
a = [int(x) for x in input().split()]
x, f = map(int, input().split())
k = 0
for i in range(n):
    if a[i] >= x + f:
        k += a[i] // (x + f)
        if a[i] % (x + f) > x:
            k += 1
    elif x < a[i] < x + f:
        k += 1
print(k * f)
