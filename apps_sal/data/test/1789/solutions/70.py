import sys

a, b, x, y = map(int, input().split())
ans = 0

if a == b:
    ans = x
elif a < b:
    move1 = (b - a) * x * 2 + x
    move2 = (b - a) * y + x

    ans = min(move1, move2)
else:
    move1 = (a - b) * x * 2 - x
    move2 = (a - b) * y + x

    ans = min(move1, move2)

    move3 = (a - b - 1) * y + x
    ans = min(ans, move3)

print(ans)
