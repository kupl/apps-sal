from collections import Counter

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0
c = Counter()
c[0] = 1

S = [0] * (N + 1)
s = 0

for idx, a in enumerate(A):
    idx += 1

    if idx >= K:
        c[S[idx - K]] -= 1

    s = (s + a) % K

    b = (s - idx) % K
    S[idx] = b
    ans += c[b]
    c[b] += 1

print(ans)
