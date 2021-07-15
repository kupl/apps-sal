a,b,c = map(int,input().split())
# b/aの商がcより大きければcを出力
if b // a > c:
    print(c)
# そうでなければb/aの商を出力
else:
    print(b // a)
