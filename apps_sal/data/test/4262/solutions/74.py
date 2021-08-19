from itertools import permutations
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
cnt = 0
(p, q) = (0, 0)
for i in permutations(range(1, N + 1), N):
    cnt += 1
    if i == P:
        p = cnt
    elif i == Q:
        q = cnt
if p == 0 or q == 0:
    print(0)
else:
    print(abs(p - q))
