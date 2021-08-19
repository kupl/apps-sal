(a1, b1) = list(map(int, input().split()))
(a2, b2) = list(map(int, input().split()))
(a3, b3) = list(map(int, input().split()))
if a1 >= a2 + a3 and b1 >= max(b2, b3):
    print('YES')
elif a1 >= a2 + b3 and b1 >= max(b2, a3):
    print('YES')
elif a1 >= b2 + a3 and b1 >= max(a2, b3):
    print('YES')
elif a1 >= b2 + b3 and b1 >= max(a2, a3):
    print('YES')
elif b1 >= a2 + a3 and a1 >= max(b2, b3):
    print('YES')
elif b1 >= a2 + b3 and a1 >= max(b2, a3):
    print('YES')
elif b1 >= b2 + a3 and a1 >= max(a2, b3):
    print('YES')
elif b1 >= b2 + b3 and a1 >= max(a2, a3):
    print('YES')
else:
    print('NO')
