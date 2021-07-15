
t = int(input())

for _ in range(t):
    r, g, b = sorted(map(int, input().split()))
    s = sum([r, g, b])
    print(min([r + g, s // 2]))

