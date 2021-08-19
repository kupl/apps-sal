import heapq
(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = sum(a)
pre = [0]
j = 0
while j < n:
    pre.append(a[j] + pre[-1])
    j += 1
ab = []
af = []
af1 = []
j = n - 1
while j >= 0:
    heapq.heappush(af, -(s - pre[j] - b[j]))
    af1.append(-af[0])
    j += -1
af1.reverse()
if k == 0:
    j = 0
    ans = 0
    while j < n:
        ans = max(ans, s - pre[j] - b[j])
        j += 1
    print(ans)
elif k == 1:
    j = 0
    m = float('inf')
    ans = 0
    while j < n - 1:
        m = min(m, b[j])
        if j < n - 2:
            ans = max(ans, max(0, pre[j + 1] - m) + max(0, af1[j + 1]), s - pre[j] - b[j] - a[j + 1], s - b[0] - a[j + 1])
        else:
            ans = max(ans, pre[j + 1] - m + max(0, af1[j + 1]), s - pre[j] - b[j] - a[j + 1])
        j += 1
    j = 0
    while j < n - 1:
        ans = max(ans, s - a[-1] - b[j] + max(0, a[-1] - b[-1]))
        j += 1
    print(ans)
else:
    j = 0
    ans = 0
    while j < n - 1:
        ans = max(ans, s - b[j])
        j += 1
    ans = max(ans, a[-1] - b[-1])
    print(ans)
