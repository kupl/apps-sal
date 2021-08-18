[n] = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]
h = [0] + h
det = 0
m = 100000000000
for i in range(1, n + 1):
    det = det + (h[i - 1] - h[i])
    m = min(m, det)
print(-m)
