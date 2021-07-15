n = int(input())
if n==2:
    print('3', '2 1 2', sep='\n')
elif n==3:
    print('4', '2 1 3 2', sep='\n')
else:
    b = []
    for i in range(2, n+1, 2):
        b.append(i)
    for i in range(1, n+1, 2):
        b.append(i)
    for i in range(2, n+1, 2):
        b.append(i)
    print(len(b))
    print(*b)
