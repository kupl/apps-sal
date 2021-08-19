(N, M) = list(map(int, input().split()))
from_one = []
to_n = []
for _ in range(M):
    (a, b) = [int(x) - 1 for x in input().split()]
    if a == 0:
        from_one += [b]
    elif b == 0:
        from_one += [a]
    elif a == N - 1:
        to_n += [b]
    elif b == N - 1:
        to_n += [a]
from_one = set(from_one)
to_n = set(to_n)
if len(from_one & to_n) >= 1:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
