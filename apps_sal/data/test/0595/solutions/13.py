def leap(x):
    return x % 400 == 0 or (x % 4 == 0 and x % 100 != 0)


(y, v) = (int(input()), 0)
l = leap(y)
while True:
    v = (v + 1 + leap(y)) % 7
    y += 1
    if v == 0 and leap(y) == l:
        print(y)
        break
