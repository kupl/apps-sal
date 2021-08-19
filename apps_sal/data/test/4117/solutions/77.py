from collections import Counter
N = int(input())
L = list(map(int, input().split()))
C = Counter(L)
L = sorted(set(L))
M = len(L)
ans = 0
for i in range(M):
    for j in range(i + 1, M):
        for k in range(j + 1, M):
            (a, b, c) = (L[i], L[j], L[k])
            if a < b + c and b < c + a and (c < a + b):
                ans += C[a] * C[b] * C[c]
print(ans)
