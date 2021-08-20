x = int(input())
for i in range(1, 10 ** 5):
    if x <= i * (i + 1) // 2:
        print(i)
        break
