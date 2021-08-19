from collections import Counter
(_, K) = map(int, input().split())
A = sorted(list(Counter(input().split()).values()))
print(sum(A[:len(A) - K]))
