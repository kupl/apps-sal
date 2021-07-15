n = int(input())
ar = list(map(int, input().split()))
lol = dict()
kek = set()
ahah = []
for i in range(n):
    if ar[i] - i in kek:
        ahah.append(sorted([i, lol[ar[i] - i]]))
    lol[ar[i] - i] = i
    kek.add(ar[i] - i)
ahah.sort()
A = [[] for _ in range(n)]
for a, b in ahah:
    A[b].append(a)
dp = [ar[i] for i in range(n)]
for i in range(n):
    for elem in A[i]:
        dp[i] = max(dp[i], dp[elem] + dp[i])
print(max(dp))
