n = int(input())
task = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])

t = 0
for a, b in task:
    t += a
    if t > b:
        print('No')
        return
print('Yes')
