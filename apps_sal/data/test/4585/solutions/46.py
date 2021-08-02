x = int(input())
i = 1
while True:
    if (i + 1) * i // 2 >= x:
        print(i)
        break
    i += 1
