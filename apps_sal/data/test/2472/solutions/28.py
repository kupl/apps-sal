n = int(input())
ab = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])

t = 0
for a, b in ab:
    t += a
    if t > b:
        print('No')
        return
print('Yes')
