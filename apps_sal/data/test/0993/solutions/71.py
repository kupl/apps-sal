import collections
(N, M) = map(int, input().split())
L = list(map(int, input().split()))
R = [0]
sums = 0
for i in L:
    sums += i
    sums = sums % M
    R.append(sums)
c = collections.Counter(R)
A = list(c.values())
A = [i * (i - 1) // 2 for i in A]
print(sum(A))
