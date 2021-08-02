n, m, k = list(map(int, input().split()))
cnt = [0] * (10**6 + 5)
l = [int(i) for i in input().split()]
for i in l:
    cnt[i] += 1
sm = 0
for i in range(10**6 + 5):
    sm += cnt[i]
    if(i >= m):
        sm -= cnt[i - m]
    if(sm >= k):
        sm -= 1
        cnt[i] = 0
print(n - sum(cnt))
