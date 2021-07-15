n, m, X, Y = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x = sorted(x, reverse=False)[-1]
y = sorted(y, reverse=False)[0]
flg = 'War'
if x < x+1 <= y:
    if x+1 > X:
        if x+1 <= Y:
            flg = 'No War'

print(flg)    

