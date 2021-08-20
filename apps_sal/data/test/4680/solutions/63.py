(a, b, c) = input().split()
(a, b, c) = (int(a), int(b), int(c))
if a == 5 and b == 7 and (c == 5):
    print('YES')
elif a == 5 and b == 5 and (c == 7):
    print('YES')
elif a == 7 and b == 5 and (c == 5):
    print('YES')
else:
    print('NO')
