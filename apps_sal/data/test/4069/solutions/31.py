import sys
array = list(map(int, input().strip().split()))
x = abs(array[0])
k = array[1]
d = array[2]
if d == 0:
    amari = abs(x)
else:
    move_cnt = int(x / d)
    if move_cnt <= k:
        k -= move_cnt
        amari = x - move_cnt * d
    else:
        amari = x - k * d
        k = 0
    if k > 0:
        if k % 2 == 1:
            if amari > 0:
                amari -= d
            else:
                amari += d
print(abs(amari))
