import bisect

n = int(input())
l = list(map(int, input().split()))

l.sort()
cnt = 0


for i in range(n - 2):
    for j in range(i + 1, n - 1):
        sum = l[i] + l[j]
        index = bisect.bisect_left(l, sum)
        cnt += index - j - 1

print(cnt)
