from heapq import heappush, heappop
N = int(input())
a = [int(x) for x in input().split()]
left = sorted(a[:N])
max_left = [sum(left)]
right = sorted([-x for x in a[-N:]])
min_right = [sum(right) * -1]
for i in range(N, 2 * N):
    j = 3 * N - i - 1
    heappush(left, a[i])
    v = heappop(left)
    max_left.append(max_left[-1] - v + a[i])
    heappush(right, a[j] * -1)
    v = heappop(right) * -1
    min_right.append(min_right[-1] - v + a[j])
ans = float('-inf')
for (l, r) in zip(max_left, min_right[::-1]):
    ans = max(l - r, ans)
print(ans)
