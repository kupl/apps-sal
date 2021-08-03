n = int(input())
h = list(map(int, input().split()))
maxh = max(h)
cnt = 0
for i in range(maxh, 0, -1):
    if h[0] >= i:
        cnt += 1
    for j in range(1, n):
        if h[j] >= i and h[j - 1] < i:
            cnt += 1
print(cnt)
