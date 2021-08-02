N = int(input())
ab = [tuple(map(int, input().split())) for _ in range(N)]
cd = [tuple(map(int, input().split())) for _ in range(N)]

ab.sort(key=lambda xy: xy[1], reverse=True)
cd.sort()

ans = 0
for c, d in cd:
    for index, (a, b) in enumerate(ab):
        if a < c and b < d:
            ab[index] = (201, 201)
            ans += 1
            break

print(ans)
