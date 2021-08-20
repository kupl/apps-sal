import itertools
N = int(input())
l = list(itertools.permutations(range(1, N + 1)))
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
print(abs(l.index(A) - l.index(B)))
