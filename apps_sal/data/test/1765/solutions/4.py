import functools
n = int(input())

nums = list(map(int, input().split()))

bits = ["{0:b}".format(num) for num in nums]


def possible(v):
    possible_vals = [
        nums[x]
        for x in range(n)
        if len(bits[x]) > v and bits[x][len(bits[x]) - v - 1] == '1'
    ]
    if len(possible_vals) == 0:
        return False, []
    res = functools.reduce((lambda x, y: x & y), possible_vals, pow(2, v + 1) - 1)
    return bool(res & ((1 << (v + 1)) - 1) == (1 << v)), possible_vals


for x in range(30, -1, -1):
    p, vals = possible(x)
    if p:
        print(len(vals))
        print(' '.join(list(map(str, vals))))
        break
