import collections
(N, K) = list(map(int, input().split()))
A = list(map(int, input().split()))
table = collections.defaultdict(int)
ans = 0
s = [0] * (N + 1)
a = set()
for i in range(N):
    s[i + 1] = s[i] + A[i]
s = [(s[i] - i) % K for i in range(N + 1)]
for i in range(N + 1):
    ans += table[s[i]]
    table[s[i]] += 1
    if i >= K - 1:
        table[s[i - K + 1]] -= 1
print(ans)
