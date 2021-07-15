from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

dictionary = list(permutations(list(range(1, N+1))))
a = dictionary.index(P)
b = dictionary.index(Q)
print((abs(a-b)))

