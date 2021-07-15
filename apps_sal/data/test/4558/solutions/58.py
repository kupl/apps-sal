# A - Sandglass2

# X秒測れる砂時計で、t秒後に残っている砂は何グラムか


X,t = list(map(int,input().split()))

if X <= t:
    print('0')
else:
    print((X - t))

