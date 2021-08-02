import sys
input = sys.stdin.readline
n, x = map(int, input().split())
d = list(map(int, input().split()))
mx = 0
i = n - 1
j = n - 1
k = 0
cursum = 0
miss = x
while d[j] < miss:
    miss -= d[j]
    cursum += (d[j] * (d[j] + 1)) // 2
    j -= 1
k = d[j] - miss
cursum += (d[j] * (d[j] + 1)) // 2
cursum -= (k * (k + 1)) // 2
miss = 0
mx = cursum
while i >= 0:
    miss = d[i]
    cursum -= (d[i] * (d[i] + 1)) // 2
    cursum += (k * (k + 1)) // 2
    cursum -= (d[j] * (d[j] + 1)) // 2
    miss -= k
    miss += d[j]
    while d[j] < miss:
        miss -= d[j]
        cursum += (d[j] * (d[j] + 1)) // 2
        j -= 1
        if j < 0:
            j = n - 1
    k = d[j] - miss
    cursum += (d[j] * (d[j] + 1)) // 2
    cursum -= (k * (k + 1)) // 2
    miss = 0
    mx = max(mx, cursum)
    i -= 1
print(mx)
