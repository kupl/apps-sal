# nは展望台の数　mは道の数
n,m = list(map(int,input().split()))
high = list(map(int,input().split()))

a = []

for x in range(m):
    b = list(map(int,input().split()))
    a.append(b)


loser = []

for y in a:
    high1 = high[y[0]-1]
    high2 = high[y[1]-1]
    if high1 > high2:
        loser.append(y[1])
    elif high1 ==  high2:
        loser.append(y[0])
        loser.append(y[1])
    else:
        loser.append(y[0])

new_loser = list(set(loser))
print((n-len(new_loser)))

