n = int(input().strip())
vals = [int(x) for x in input().strip().split()]
term = vals[1]
d = vals[1] - vals[0]
ap = True
for x in range(2, n):
    next_term = vals[x]
    if next_term - term != d:
        ap = False
    term = next_term
if ap:
    print(term + d)
else:
    print(term)
