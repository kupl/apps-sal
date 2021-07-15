# 052

# 1.値を正しく取得
a,b,c,d=(int(x) for x in input().split())

# 2.正しく処理

menseki1 = a * b
menseki2 = c * d

if menseki1 > menseki2:
    print(menseki1)

elif menseki1 < menseki2:
    print(menseki2)

else :
    print(menseki1)

