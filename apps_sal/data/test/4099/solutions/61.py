(N, maxscore, avgscore) = map(int, input().split())
A = list(map(int, input().split()))
goaltotal = N * avgscore
currenttotal = sum(A)
if goaltotal - currenttotal > maxscore:
    print(-1)
elif goaltotal - currenttotal < 0:
    print(0)
else:
    print(goaltotal - currenttotal)
