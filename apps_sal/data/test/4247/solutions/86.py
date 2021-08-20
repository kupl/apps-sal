input()
P = list(map(int, input().split()))
print(sum((A < B < C or C < B < A for (A, B, C) in zip(P, P[1:], P[2:]))))
