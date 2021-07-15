import itertools

N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

L = [i for i in range(1,N+1)]
L2 = itertools.permutations(L,N)
L3 = []
for i in L2:
    L3.append(i)

# print(N,P,Q,L,L2,L3)
# print(L3.index(tuple(P)))
# print(L3.index(tuple(Q)))
print(abs(L3.index(tuple(P)) - L3.index(tuple(Q))))
