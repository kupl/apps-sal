from collections import Counter
N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())

c = Counter(A)
cc = list(c.values())
ans = 0
for i in range(len(cc)):
    if cc[i] % 2 == 1:
        ans += 1

print(ans)
