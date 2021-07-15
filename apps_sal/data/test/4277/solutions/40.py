# 電車代とタクシー代で小さい方を選ぶ
# 電車が安い
n,a,b = map(int, input().split())

if a * n <= b:
    print(a * n)
# タクシーが安い
else:
    print(b)
