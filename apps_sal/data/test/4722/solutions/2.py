A, B = map(int, input().split())

# A, B, A+B のいずれかの枚数のクッキーをヤギたちに渡すことができる
# 3匹のヤギ が同じ枚数ずつ食べられるようにクッキーを渡すことが可能ならば 'Possible' と、そうでなければ 'Impossible' と出力

if A % 3 == 0:
    print('Possible')
elif B % 3 == 0:
    print('Possible')
elif (A + B) % 3 == 0:
    print('Possible')
else:
    print('Impossible')
