a, b, c = list(map(int, input().split()))
r = 3 * max(a, b, c) - sum([a, b, c])
if r % 2:
    print((r // 2 + 2))
else:
    print((r // 2))

