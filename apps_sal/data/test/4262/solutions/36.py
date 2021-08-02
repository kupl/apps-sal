import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

X = list(itertools.permutations(P))
X.sort()

a = X.index(P)
b = X.index(Q)


print(abs(a - b))
