(a1, b1) = map(int, input().split())
(a2, b2) = map(int, input().split())
(a3, b3) = map(int, input().split())
if a1 < b1:
    (a1, b1) = (b1, a1)
if max([a2, b2, a3, b3]) > a1:
    print('NO')
elif a2 + a3 <= a1 and max(b2, b3) <= b1:
    print('YES')
elif a2 + b3 <= a1 and max(b2, a3) <= b1:
    print('YES')
elif b2 + a3 <= a1 and max(a2, b3) <= b1:
    print('YES')
elif b2 + b3 <= a1 and max(a2, a3) <= b1:
    print('YES')
elif a2 + a3 <= b1 and max(b2, b2) <= a1:
    print('YES')
elif a2 + b3 <= b1 and max(b2, a3) <= a1:
    print('YES')
elif b2 + a3 <= b1 and max(a2, b3) <= a1:
    print('YES')
elif b2 + b3 <= b1 and max(a2, a3) <= a1:
    print('YES')
else:
    print('NO')
