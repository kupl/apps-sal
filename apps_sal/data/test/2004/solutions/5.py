n = int(input())
if n == 2:
    print(3)
    print(2, 1, 2)
else:
    print(n + n // 2)
    for i in range(2, n + 1, 2):
        print(i, end= ' ')
    for i in range(1, n + 1, 2):
        print(i, end= ' ')
    for i in range(2, n + 1, 2):
        print(i, end= ' ')
    

