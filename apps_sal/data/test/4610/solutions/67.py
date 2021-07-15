from collections import Counter as CC

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = CC(A)
C = sorted(B.values())
print(sum(C[:max(0, len(C) - K)]))
