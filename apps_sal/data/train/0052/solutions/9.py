n = int(input())
a = sorted([int(input()) for i in range(n)])
time = 0
for i in range(n):
    time += a[i] * a[n - 1 - i]
print(time % 10007)
