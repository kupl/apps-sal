import itertools as it
n = int(input())
A = list(map(int, input().split()))
A = sorted(A)
print(max([len(list(x[1])) for x in it.groupby(A)]))
