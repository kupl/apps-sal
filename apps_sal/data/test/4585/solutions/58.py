X = int(input())
for i in range(1, 100000):
    if X <= i * (i + 1) // 2:
        print(i)
        break
