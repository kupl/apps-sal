from collections import Counter
n = int(input())
A = list(map(int, input().split()))
A_pos = [A[x] + x for x in range(n)]
A_neg = [-A[x] + x for x in range(n)]
C_pos = Counter(A_pos)
C_neg = Counter(A_neg)
ans = 0
for c in C_pos:
    ans += C_pos[c] * C_neg[c]
print(ans)
