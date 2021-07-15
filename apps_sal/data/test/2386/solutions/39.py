from statistics import median
n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    a[i] -= i+1

a.sort()

m = int(median(a))

print(sum(abs(a[i] - m) for i in range(n)))
