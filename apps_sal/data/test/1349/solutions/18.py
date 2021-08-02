t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    d = []
    for i in range(1, len(x)):
        d.append((x[i] - x[i - 1]) // 2 + 1)
    d.append(x[0])
    d.append(n - x[-1] + 1)
    print(max(d))
