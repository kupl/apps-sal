from numpy import median
n = int(input())
alist = list(map(int, input().split()))

for i in range(n):
    alist[i] -= i + 1

med = int(median(alist))
ans = 0
for a in alist:
    ans += abs(a - med)
print(ans)
