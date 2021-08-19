(A, B, C) = map(int, input().split())
if A == 5 and B == 5 and (C == 7):
    print('YES')
elif A == 5 and B == 7 and (C == 5):
    print('YES')
elif A == 7 and B == 5 and (C == 5):
    print('YES')
else:
    print('NO')
