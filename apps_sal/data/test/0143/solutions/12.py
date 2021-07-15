n = int(input())
a = sorted(int(x) for x in input().split())
m = 0
for i in range(1, n+1):
    if i > a[i-1] + m:
        m = i - a[i-1]
print(n-m+1)
