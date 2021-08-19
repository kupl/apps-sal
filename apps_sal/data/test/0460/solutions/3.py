from sys import stdin
input = stdin.readline
(p, x, y) = [int(i) for i in input().split()]


def shirt(score, place):
    i = int(score / 50) % 475
    for j in range(25):
        i = (i * 96 + 42) % 475
        if place == i + 26:
            return True
    return False


ans = -1
c = x
while c >= y:
    if shirt(c, p):
        ans = 0
        break
    else:
        c -= 50
if ans == -1:
    c = 0
    while True:
        if shirt(c * 100 + 50 + x, p) or shirt(c * 100 + 100 + x, p):
            ans = c + 1
            break
        else:
            c += 1
print(ans)
