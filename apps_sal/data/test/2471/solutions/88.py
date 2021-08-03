H, W, N = map(int, input().split())
d = {}

for i in range(N):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    for j in range(-1, 2):
        for k in range(-1, 2):
            if 1 <= a + j < H - 1 and 1 <= b + k < W - 1:
                if d.get((a + j, b + k)) is None:
                    d[(a + j, b + k)] = 0
                d[(a + j, b + k)] += 1


ans = [0] * 10
for v in d.values():
    ans[v] += 1
ans[0] = (H - 2) * (W - 2) - sum(ans[1:])

for i in range(10):
    print(ans[i])
