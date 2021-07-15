from collections import Counter
N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
for i in range(1, N+1):
    print(C[i])
