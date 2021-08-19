(a, b) = map(int, input().split())
for i in range(1, 10000000000000000, 2):
    if a < i:
        print('Vladik')
        break
    else:
        a -= i
    if b < i + 1:
        print('Valera')
        break
    else:
        b -= i + 1
