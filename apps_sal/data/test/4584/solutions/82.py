# ABC163
import collections
N = int(input())
A = list(map(int, input().split()))
c = collections.Counter(A)
for i in range(N):
    print(c[i + 1])
