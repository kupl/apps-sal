A, B, C = map(int, input().split())

num = int(B / A)

if num >= C:
    print(C)
elif num >= 1:
    print(num)
else:
    print('0')
