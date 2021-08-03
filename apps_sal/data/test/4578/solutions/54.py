N, x = list(map(int, input().split()))
donuts = 0
donuts_min = 999999
counta = 0

for i in range(N):
    donuts = int(input())
    x -= donuts
    counta += 1
    if donuts_min >= donuts:
        donuts_min = donuts
    else:
        pass

countb = x // donuts_min
print((counta + countb))
