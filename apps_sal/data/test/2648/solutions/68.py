from collections import Counter
N = int(input())
A = list(map(int, input().split()))
d = dict(Counter(A))
kaburi = 0
for key in d:
    kaburi += d[key] - 1
print(N - (kaburi % 2 + kaburi))
