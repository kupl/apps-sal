# 入力
A, B = map(int, input().split())

# 同じなら引き分け、1が出たら勝ち、大きい方が勝ち
if A == B:
    print('Draw')
elif A == 1:
    print('Alice')
elif B == 1:
    print('Bob')
elif A > B:
    print('Alice')
elif A < B:
    print('Bob')
