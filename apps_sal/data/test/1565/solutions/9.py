l = int(input())
n = str(input())
best_len = l
best = int(n)
to_try = []
for i in range(l - 1):
    if n[i + 1] != '0':
        candidate = max(i + 1, l - i - 1) + 1
        if candidate < best_len:
            to_try.clear()
            to_try.append(i+1)
            best_len = candidate
        elif candidate == best_len:
            to_try.append(i+1)
for i in to_try:
    best = min(best, int(n[:i]) + int(n[i:]))
print(best)
