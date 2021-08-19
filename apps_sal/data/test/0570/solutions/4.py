(a, b) = list(map(int, input().split()))
i = 1
cur = 0
while (1 - cur) * a + cur * b >= i:
    if cur == 0:
        a -= i
    else:
        b -= i
    i += 1
    cur = 1 - cur
if cur == 0:
    print('Vladik')
else:
    print('Valera')
