# A - Sharing Cookies

# A,B,A+Bのいずれかが3の倍数かどうか判定する


A, B = list(map(int, input().split()))

if A % 3 == 0\
        or B % 3 == 0\
        or (A + B) % 3 == 0:
    print('Possible')
else:
    print('Impossible')
