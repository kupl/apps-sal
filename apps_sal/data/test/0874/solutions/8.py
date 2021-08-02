a = int(input())
if a % 2 == 1: print(-1)
else:
    i = -1
    while i < a - 1:
        i = i + 3
        print(i, end=' ')
        i = i - 1
        print(i, end=' ')
