(a, b) = list(map(int, input().split()))
if a == 13 and b == 1:
    print('Bob')
elif a == 1 and b == 13:
    print('Alice')
elif a > b:
    print('Alice')
elif a == b:
    print('Draw')
else:
    print('Bob')
