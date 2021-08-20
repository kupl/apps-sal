(N, K) = map(int, input().split())
(R, S, P) = map(int, input().split())
T = list(input())
dic = {'r': P, 's': R, 'p': S}
ans = 0
for i in range(K):
    ans += dic[T[i]]
for i in range(K, N):
    if T[i - K] != T[i]:
        ans += dic[T[i]]
    else:
        T[i] = 'e'
print(ans)
