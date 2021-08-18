import collections
N = int(input())
A = list(map(int, input().split()))
c = collections.Counter(A)
A = set(A)
MAX_A = 10**6
X = [0] * (MAX_A + 1)
for i in A:
    for j in range(i, MAX_A + 1, i):
        X[j] += 1

ans = len([a for a in A if (X[a] == 1) and (c[a] == 1)])
print(ans)
