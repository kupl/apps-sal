(N, K) = list(map(int, input().split()))
cnt = [0] * N
for k in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        cnt[a - 1] += 1
ans = 0
for c in cnt:
    if c == 0:
        ans += 1
print(ans)
