import bisect
n = int(input())
l = list(map(int, input().split()))
l = sorted(l)
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        x = bisect.bisect_left(l, l[i] + l[j])
        cnt += x - j - 1
print(cnt)
