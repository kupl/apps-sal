from collections import Counter
n = int(input())
A = list(map(int, input().split()))
P = [i + a + 1 for (i, a) in enumerate(A)]
Q = [j - a + 1 for (j, a) in enumerate(A)]
cQ = Counter(Q)
ans = 0
for p in P:
    ans += cQ[p]
print(ans)
