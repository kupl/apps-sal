import math
a, b, x = map(int, input().split())
ok = 0
no = pow(10, 9) + 1

while no != ok + 1:
    center = math.floor((ok + no) / 2)
    digit = 1
    while center // pow(10, digit) != 0:
        digit += 1

    if x >= a * center + b * digit:
        ok = center
    elif x < a * center + b * digit:
        no = center

print(ok)
