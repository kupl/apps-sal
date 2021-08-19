from collections import defaultdict
import bisect
(N, K) = map(int, input().split())
A = list(map(int, input().split()))
s = 0
S = [0]
for (i, a) in enumerate(A):
    s += a
    S.append(s % K)
cnt = 0
dic = {}
for (i, s) in enumerate(S):
    x = (s - i) % K
    if x in dic:
        cnt += dic[x]
        dic[x] += 1
    else:
        dic[x] = 1
    K_prev = i - K + 1
    if K_prev >= 0:
        y = (S[K_prev] - K_prev) % K
        dic[y] -= 1
print(cnt)
