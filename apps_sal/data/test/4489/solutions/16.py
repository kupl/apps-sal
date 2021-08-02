bag = {}
N = int(input())
for _ in range(N):
    s = input()
    if s in bag:
        bag[s] += 1
    else:
        bag[s] = 1
M = int(input())
for _ in range(M):
    s = input()
    if s in bag:
        bag[s] -= 1

d_swap = {v: k for k, v in list(bag.items())}
if max(d_swap) < 0:
    print((0))
else:
    print((max(d_swap)))
