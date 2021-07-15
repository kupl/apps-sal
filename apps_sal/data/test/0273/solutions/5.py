a, b = input().split()

best = None
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        username = a[:i] + b[:j]
        if best is None or username < best:
            best = username

print(best)

