"""
    This code is part of the codeforces problems solved in the repository[1]. 
    All solutions are written in python3.
    
    [1]: https://github.com/praveendath92/codeforces
"""


def read_line():
    return input().strip()


def read_int():
    return int(read_line())


def read_int_array():
    return [int(i) for i in read_line().split(' ')]


def read_string_array():
    return [i for i in read_line().split(' ')]


T = read_int()
D = read_int_array()

AD = [-1] * len(D)
AD[0] = D[0]
rests = 1 if AD[0] == 0 else 0

for i in range(1, len(D)):
    if D[i] == 0:
        rests += 1
        AD[i] = 0
    elif D[i] == 1:
        if AD[i - 1] == 1:
            rests += 1
            AD[i] = 0
        else:
            AD[i] = 1
    elif D[i] == 2:
        if AD[i - 1] == 2:
            rests += 1
            AD[i] = 0
        else:
            AD[i] = 2
    elif D[i] == 3:
        if AD[i - 1] == 3:
            AD[i] = 3
        else:
            AD[i] = D[i] - AD[i - 1]

print(rests)
