from collections import Counter
N = int(input())
A = list(map(int, input().split()))
B = Counter(list(i + 1 + A[i] for i in range(N)))
C = Counter((i + 1 - A[i] for i in range(N)))
ans = 0
for j in range(N):
    ans += B[j] * C[j]
print(ans)
