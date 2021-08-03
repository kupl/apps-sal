x, y = list(map(int, input().split(' ')))
cnt = 0
tmp = x
while tmp <= y:
    cnt = cnt + 1
    tmp = tmp * 2
print(cnt)
