from collections import *
N, K = list(map(int, input().split()))

a = deque()
for i in range(60):  # 2**60 > 1e18
    if N & (1 << i):
        a.appendleft([i, 1])
k = len(a)

if k > K:
    print("No")
    return

# high
while k + a[0][1] <= K:
    e, c = a.popleft()
    if len(a) == 0 or a[0][0] != e - 1:
        a.appendleft([e - 1, 0])
    a[0][1] += 2 * c
    k += c

# low
if K - k:
    a[-1][1] -= 1
    count = K - k
    first = a[-1][0] - 1
    last = first - count + 1
    for i in range(first, last - 1, -1):
        a.append([i, 1])
    a.append([last, 1])
    k = K

ans = []
for i in a:
    ans += [i[0]] * i[1]
ans = list(map(str, ans))
ans = "Yes\n" + " ".join(ans)
print(ans)
