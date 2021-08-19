import itertools
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
X = list(itertools.permutations(P))
X.sort()
a = 0
b = 0
for i in range(len(X)):
    if list(X[i]) == P:
        a = i
    if list(X[i]) == Q:
        b = i
print(abs(a - b))
