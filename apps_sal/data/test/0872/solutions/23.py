N = int(input())
X = [int(a) for a in input().split()]
A = [x for x in X if x % 2 == 0]
B = [x for x in X if x % 2 == 1]
if len(A) * len(B):
    print(*sorted(X))
else:
    print(*X)
