from collections import Counter
N = int(input())
A = list(map(int, input().split()))
B = [a + i for (i, a) in enumerate(A)]
C = [j - a for (j, a) in enumerate(A)]
(B, C) = (Counter(B), Counter(C))
ans = 0
for k in B.keys():
    ans += B[k] * C[k]
print(ans)
