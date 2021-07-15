n = int(input())
if n == 2:
    print(1)
    print(1)
elif n == 3:
    print(2)
    print(1, 3)
else:
    a = []
    if n % 2 == 1:
        a.append(n)
        n -= 1
    for i in range(n // 2 - 1, -1, -1):
        a.append(i + 1)
        a.append(i + 1 + n // 2)
    print(len(a))
    print(*a)
    

