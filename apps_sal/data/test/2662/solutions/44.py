from bisect import bisect_right
n = int(input())
color = [0] * (n + 1)
for i in range(n):
    a = int(input())
    j = bisect_right(color, a)
    color[j - 1] = a + 1
ans = 0
for t in color:
    if t != 0:
        ans += 1
print(ans)
