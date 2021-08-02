import bisect
n = int(input())
l1 = list(map(int, input().split()))
l2 = []
for i in range(0, n):
    if l1[i] != 0:
        l2.append(abs(l1[i]))
l2.sort()
ans = 0
for i in range(0, len(l2)):
    x = bisect.bisect_right(l2, 2 * l2[i], 0, len(l2))
    ans += (x - i - 1)
print(ans)
