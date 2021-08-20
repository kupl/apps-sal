from math import ceil
N = int(input())
T = input()
if T == '1':
    print(20000000000)
else:
    s = '110' * ceil(2 * N / 3)
    if T not in s:
        print(0)
    elif T[-1] == '0':
        print(10000000000 - (N - 1) // 3)
    else:
        print(10000000000 - T.count('0'))
