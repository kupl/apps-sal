n = int(input())
direction = input()
xi = [int(x) for x in input().split(' ')]
m = []
for i in range(n - 1):
    if direction[i:i + 2] != 'RL':
        continue
    m.append(xi[i + 1] - xi[i])
if not m:
    print(-1)
else:
    print(int(min(m) / 2))
