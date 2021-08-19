N, K = map(int, input().split())
*P, = map(int, input().split())

Q = [(i + 1) / 2 for i in P]

p = ans = sum(Q[:K])

for i in range(N - K):
    p = p - Q[i] + Q[i + K]
    # print(i, ans, t,i+K,Q[i],Q[i+K])
    ans = max(ans, p)
print(ans)
