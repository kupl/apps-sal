a, b, c, d = map(int, input().split())
cnt = d - a
if cnt > 0:
    num = 1 * a
    cnt -= b
    if cnt > 0:
        num = a + (d - a - b) * (-1)
else:
    num = 1 * d
print(num)
