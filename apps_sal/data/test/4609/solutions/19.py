from collections import Counter
N = int(input())
A = [int(input()) for _ in range(N)]
print(sum((c % 2 for c in Counter(A).values())))
