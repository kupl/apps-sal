x = int(input())
for i in range(x, 1000):
    if i // 100 == i % 10 and i // 100 == (i // 10) % 10:
        break
print(i)
