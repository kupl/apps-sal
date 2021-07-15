a = int(input())
if a == 1 or a == 2:
    print(1)
    print(1)
elif a == 3:
    print(2)
    print(1, 3)
elif a == 4:
    print(4)
    print(3, 1, 4, 2)
else:
    print(a)
    b = []
    for i in range(a//2+a%2):
        b.append(i*2+1)
    for k in range(a//2):
        b.append(k*2+2)
    print(*b)

