X, Y = map(int, input().split())

cnt = 0
calc = X

while calc <= Y:
    cnt += 1
    calc = X*(2**cnt)

print(cnt)
