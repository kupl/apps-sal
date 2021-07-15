import collections
N = int(input())
A = [0]
A += list(map(int, input().split()))
cnt = 0
L = [- 10 ** 6]
R = [- 10 ** 6]

for i in range(1, N + 1):
    L.append(i + A[i])
    R.append(i - A[i])
c = collections.Counter(L)

for j in range(1, N + 1):
    cnt += c.get(R[j], 0)
print(cnt)
