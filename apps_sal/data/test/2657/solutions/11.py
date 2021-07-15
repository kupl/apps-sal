from bisect import bisect_left
N = int(input())
a = list(map(int,input().split()))
a.sort()
x = a[-1]
i = bisect_left(a, x/2, hi=N-2)
for j in [i-1, i, i+1]:
    if 0 <= j < N and abs(a[j]-x/2) < abs(a[i]-x/2):
        i = j
print(x, a[i])
