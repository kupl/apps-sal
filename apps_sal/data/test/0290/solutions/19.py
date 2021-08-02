def getS(n):
    return int(n ** (1 / 2))


squares = int(input())


ans = 0


side = getS(squares)
ans += side * 2

remains = squares - (side ** 2)

if remains % side == 0:
    ans += remains // side
else:
    ans += remains // side + 1

print(ans)
