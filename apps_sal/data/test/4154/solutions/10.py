(N, M) = map(int, input().split())
card = [0] * (N + 2)
ans = [0] * (N + 1)
for i in range(M):
    (L, R) = map(int, input().split())
    card[L] += 1
    card[R + 1] -= 1
cnt = 0
for h in range(N + 1):
    cnt += card[h]
    ans[h] = str(cnt)
print(ans.count(str(M)))
