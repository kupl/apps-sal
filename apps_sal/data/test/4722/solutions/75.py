# 入力
A, B = map(int, input().split())

# A,B,A+Bのうちどれか1つでも3で割り切れればPossible
if A % 3 == 0:
    print('Possible')
elif B % 3 == 0:
    print('Possible')
elif (A + B) % 3 == 0:
    print('Possible')
else:
    print('Impossible')
