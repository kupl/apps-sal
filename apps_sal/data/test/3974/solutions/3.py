p = [0] + [1 if i == '+' else -1 for i in input()]
for i in range(1, len(p)):
    p[i] += p[i - 1]
print(max(p) - min(p))
