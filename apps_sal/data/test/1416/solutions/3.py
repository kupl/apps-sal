n, w = map(int, input().split())
cups = sorted([int(x) for x in input().split()])

girl = cups[0]
boys = cups[n]

both = min(girl, boys / 2)

print(min(n * both + 2 * n * both, w))
