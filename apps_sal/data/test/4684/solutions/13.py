# A - RGB Cards

# 整数r,g,bを入力し、左から並べてできた3桁の整数が4の倍数であるか判定する


r,g,b = list(map(str,input().split()))

answer = int(r + g + b)

if answer % 4 == 0:
    print('YES')
else:
    print('NO')

