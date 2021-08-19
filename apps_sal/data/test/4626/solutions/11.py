Q = int(input())
for _ in range(Q):
    (a, b, c) = tuple(map(int, input().split()))
    A = [a - 1, a, a + 1]
    B = [b - 1, b, b + 1]
    C = [c - 1, c, c + 1]
    comps = []
    for x in A:
        for y in B:
            for z in C:
                comps.append((x, y, z))
    ans = float('inf')
    for (a, b, c) in comps:
        ans = min(ans, abs(a - b) + abs(a - c) + abs(b - c))
    print(ans)
