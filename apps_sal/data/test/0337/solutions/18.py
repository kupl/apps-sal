w, h = [int(v) for v in input().split()]
u1, d1 = [int(v) for v in input().split()]
u2, d2 = [int(v) for v in input().split()]

stones = {d1: u1, d2: u2}
curr = w

for i in reversed(list(range(h + 1))):
    curr = max(0, curr + i - stones.get(i, 0))

print(curr)

