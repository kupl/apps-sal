import collections
N = int(input())
A = list(map(int, input().split()))

C = collections.Counter(A)

V = C.values()
L = list(V)


for i in range(len(L)):
    if L[i] > 1:
        print('NO')
        return

print('YES')
