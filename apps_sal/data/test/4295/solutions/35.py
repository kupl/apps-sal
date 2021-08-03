N, K = list(map(int, input().split()))

x = N
pre_x = x

if x // K > 0:
    x = abs(x - K * (x // K))
    pre_x = x

while True:
    pre_x = x
    x = abs(x - K)

    if pre_x < x:
        print(pre_x)
        return
