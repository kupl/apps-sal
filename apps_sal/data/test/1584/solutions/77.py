from bisect import bisect_left
n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        ans += bisect_left(l, l[i] + l[j]) - j - 1

print(ans)
