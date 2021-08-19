# 入力
A, B = list(map(int, input().split()))

# 出力

if A == B:
    print('Draw')
elif A == 1:
    print('Alice')
elif B == 1:
    print('Bob')
elif A > B:
    print('Alice')
elif B > A:
    print('Bob')
