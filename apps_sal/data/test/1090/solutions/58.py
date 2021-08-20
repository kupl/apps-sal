(N, K) = map(int, input().split())
S = input()
t = S[0]
c = 0
for i in range(N):
    if S[i] != t:
        c += 1
        t = S[i]
if c <= 2 * K:
    print(N - 1)
else:
    a = c - 2 * K
    print(N - a - 1)
