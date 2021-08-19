(X, Y) = map(int, input().split())
cnt = 0
x_temp = X
while True:
    x_temp *= 2
    if x_temp <= Y:
        cnt += 1
    else:
        break
print(cnt + 1)
