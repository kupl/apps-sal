from bisect import bisect_right

n, m, k = [int(x) for x in input().split()]
x,s = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]
ans = n * x
for i in range(m):
    if b[i] <= s:
        cur_s = s - b[i]
        j = bisect_right(d, cur_s) - 1
        if j != -1:
            if (n-c[j])*a[i] < ans:
                ans = (n-c[j])*a[i]
        else:
            if (n)*a[i] < ans:
                ans = (n)*a[i]

for i in range(k):
    if d[i] <= s:
        if (n - c[i]) * x < ans:
            ans = (n - c[i]) * x
print(ans)

