# 入力
A, B, C, D = map(int,input().split())

# 処理
if A + B == C + D:
    print('Balanced')
elif A + B > C + D:
    print('Left')
else:
    print('Right')
