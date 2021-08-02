S, T = [input() for _ in range(2)]
count = 0
for i, j in zip(S, T):
    if i == j:
        count += 1
print(count)
