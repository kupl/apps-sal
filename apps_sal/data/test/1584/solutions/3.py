import bisect
n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0


for i in range(n):
    a = l[i]
    for j in range(i + 1, n):
        b = l[j]

        ans += bisect.bisect_left(l, a + b) - j - 1

print(ans)
