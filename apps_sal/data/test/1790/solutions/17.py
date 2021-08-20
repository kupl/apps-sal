n = int(input().strip())
ans = set(list(range(1, 101)))
for _ in range(n):
    stops = [int(x) for x in input().strip().split()]
    r = stops[0]
    ans = ans.intersection(set(stops[1:]))
for s in ans:
    print(s, end=' ')
print('')
