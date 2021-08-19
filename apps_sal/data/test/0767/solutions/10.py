from bisect import bisect_left
(n, k) = list(map(int, input().split()))
x = list(map(int, input().split()))
x.sort()
now = temp = n // 2
cnt = 0
for i in range(temp):
    while now != n and x[now] - x[i] < k:
        now += 1
    if now == n:
        break
    cnt += 1
    now += 1
print(cnt)
