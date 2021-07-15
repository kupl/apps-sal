import itertools

N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

p = list(itertools.permutations(range(1,N+1)))
a = p.index(P) + 1
b = p.index(Q) + 1
print(abs(a-b))
