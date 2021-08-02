from bisect import bisect
n = int(input())
a = list(map(int, input().split()))
a = sorted(a); m = 0
for i in range(n):
    m = max(m, bisect(a, a[i] + 5) - i)
print(m)
