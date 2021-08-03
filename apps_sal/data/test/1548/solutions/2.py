N = int(input())
sticks = sorted(list(map(int, input().split())))
lo, hi = 0, N - 1

X = 0
Y = 0

step = 0
while lo <= hi:
    if step == 0:
        # horizontal
        X += sticks[hi]
        hi -= 1
    else:
        # vertical
        Y += sticks[lo]
        lo += 1
    step = 1 - step

print(X * X + Y * Y)
