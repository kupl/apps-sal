# Xgある砂が1秒に1g落ちる砂時計 t秒後に何g残るか

X, t = map(int, input().split())
x = X - t

if x > 0:
    print(x)
else:
    print(0)
