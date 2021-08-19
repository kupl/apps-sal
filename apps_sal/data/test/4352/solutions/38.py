(a, b) = list(map(int, input().split()))
if a == b:
    print('Draw')
elif a == 1:
    print('Alice')
elif b == 1:
    print('Bob')
elif a < b:
    print('Bob')
elif b < a:
    print('Alice')
