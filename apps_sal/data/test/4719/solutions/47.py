from collections import Counter
N = int(input())
s = Counter(input())
for i in range(N - 1):
    s &= Counter(input())
print(''.join(sorted(s.elements())))
