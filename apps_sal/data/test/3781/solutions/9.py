from collections import Counter

T = int(input())
for _ in range(T):
    N = int(input())
    cntr = Counter(int(c) for c in input().split(' '))
    ans = any(v % 2 for v in list(cntr.values())) ^ (N % 2)
    print(('First' if ans else 'Second'))

