(N, K) = list(map(int, input().split()))
(R, S, P) = list(map(int, input().split()))
T = input()
l = []
for i in range(K):
    l.append([T[K - i - 1]])
for j in range(K, N):
    if l[K - 1 - j % K][j // K - 1] != T[j]:
        l[K - 1 - j % K].append(T[j])
    else:
        l[K - 1 - j % K].append('t')
ans = 0
for k in l:
    ans += k.count('r') * P + k.count('s') * R + k.count('p') * S
print(ans)
