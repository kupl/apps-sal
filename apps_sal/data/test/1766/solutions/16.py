
input()
input_raw = [int(x) for x in input().split(' ')]

s = 0
d = 0
i = True

while input_raw != []:
    if input_raw[0] > input_raw[-1]:
        cur = input_raw[0]
        del(input_raw[0])
    else:
        cur = input_raw[-1]
        del(input_raw[-1])

    if i:
        s += cur
        i = False
    else:
        d += cur
        i = True

print(s, d)
