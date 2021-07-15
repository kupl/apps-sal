X = int(input())

for p in range(100000):
    if p * (p + 1) // 2 >= X:
        break

print(p)
