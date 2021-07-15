a, b = map(int, input().split())
i = 1
while a >= 0 and b >= 0:
    if i % 2 == 1:
        a -= i
    else:
        b -= i
    i += 1
if a < 0:
    print('Vladik')
else:
    print('Valera')
