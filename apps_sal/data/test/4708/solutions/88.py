val = [int(input()) for i in range(4)]
if val[0] > val[1]:
    print(val[1] * val[2] + (val[0] - val[1]) * val[3])
else:
    print(val[0] * val[2])
