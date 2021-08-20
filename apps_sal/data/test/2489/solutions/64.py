from collections import Counter
N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
A = set(A)
MAX_A = 10 ** 6
X = [0] * (MAX_A + 1)
for a in A:
    for i in range(a, MAX_A + 1, a):
        X[i] += 1
ans = len([a for a in A if X[a] == 1 and C[a] == 1])
print(ans)
