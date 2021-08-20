t = list(map(int, input().split()))
x = min(t)
if x > 0:
    p = [x - 1 + (i - x + 1) % 3 for i in t]
    print(sum(((t[i] - p[i]) // 3 for i in range(3))) + min(p))
else:
    print(sum((i // 3 for i in t)))
