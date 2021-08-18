t = set(input()for _ in [0] * int(input().split()[0]))
print(['No', 'Yes'][all(sum(c < '.'for c in s) < 2for s in zip(*t))])
