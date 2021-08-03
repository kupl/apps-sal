h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

ans = []
for i in range(n):
    ans += [i + 1] * a[i]

ans = [ans[i * w:(i + 1) * w] if i % 2 == 0 else ans[(i + 1) * w - 1:i * w - 1:-1] for i in range(h)]
for c in ans:
    print(*c)
