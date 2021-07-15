year = int(input())

for i in range(year + 1, 9013):
    if i % 10 != i // 1000 and i % 10 != i % 1000 // 100 and i % 10 != i % 100 // 10 and i // 1000 != i % 1000 // 100 and i // 1000 != i % 100 // 10 and i % 100 // 10 != i % 1000 // 100:
        print(i)
        break

