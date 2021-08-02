from collections import Counter, deque

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
INF = 10**18

cnt = Counter()
cnt[0] = 1
que = deque([0])
sumR = 0
ans = 0
for right, a in enumerate(A, start=1):
    if len(que) >= K:
        cnt[que.popleft()] -= 1
    sumR = (a + sumR) % K
    D = (sumR - right) % K
    ans += cnt[D]
    cnt[D] += 1
    que.append(D)
print(ans)
