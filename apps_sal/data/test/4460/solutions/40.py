x = list(map(int, input().split()))
i = 0
for value in x:
    i = i + 1
    if value == 0:
        print(i)
        break
