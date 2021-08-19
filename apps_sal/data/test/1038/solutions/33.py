(a, b) = map(int, input().split())
(p, q) = ((a + 1) // 4, (b + 1) // 4)
(x, y) = ((a + 1) % 4, (b + 1) % 4)
if abs(a - b) < 4:
    ans = a
    for i in range(a + 1, b + 1):
        ans ^= i
    print(ans)
elif x == 0:
    ans = a
    if y == 1:
        ans ^= b
    elif y == 2:
        ans ^= b
        ans ^= b - 1
    elif y == 3:
        ans ^= b
        ans ^= b - 1
        ans ^= b - 2
    elif y == 0:
        ans ^= 0
    print(ans)
elif x == 1:
    ans = 0
    if y == 1:
        ans ^= b
    elif y == 2:
        ans ^= b
        ans ^= b - 1
    elif y == 3:
        ans ^= b
        ans ^= b - 1
        ans ^= b - 2
    elif y == 0:
        ans ^= 0
    print(ans)
elif x == 2:
    ans = a
    ans ^= a + 1
    ans ^= a + 2
    if y == 1:
        ans ^= b
    elif y == 2:
        ans ^= b
        ans ^= b - 1
    elif y == 3:
        ans ^= b
        ans ^= b - 1
        ans ^= b - 2
    elif y == 0:
        ans ^= 0
    print(ans)
elif x == 3:
    ans = a
    ans ^= a + 1
    if y == 1:
        ans ^= b
    elif y == 2:
        ans ^= b
        ans ^= b - 1
    elif y == 3:
        ans ^= b
        ans ^= b - 1
        ans ^= b - 2
    elif y == 0:
        ans ^= 0
    print(ans)
