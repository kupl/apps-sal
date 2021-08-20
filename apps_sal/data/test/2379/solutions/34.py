(N, K, C) = map(int, input().split())
S = input()
(L, R) = ([-1] * K, [-1] * K)
k = 0
temp = -C
for (i, s) in enumerate(S, 1):
    if s == 'o' and i > temp + C:
        L[k] = i
        k += 1
        temp = i
    if k == K:
        break
k = K - 1
temp = N + C + 1
for (i, s) in reversed(list(enumerate(S, 1))):
    if s == 'o' and i < temp - C:
        R[k] = i
        k -= 1
        temp = i
    if k == -1:
        break
ans = []
for (l, r) in zip(L, R):
    if l == r:
        ans.append(l)
for a in ans:
    print(a)
