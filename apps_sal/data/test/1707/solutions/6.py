import bisect
n = int(input())
a = list(map(int, input().split()))
a = [abs(i) for i in a]
a.sort()
ans = 0
for i in range(len(a)):
    right = a[i] * 2
    ans += bisect.bisect_right(a, right) - (i + 1)
print(ans)
