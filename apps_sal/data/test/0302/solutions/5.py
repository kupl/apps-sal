n = int(input())
d = {}


def count(x):
    if x == 0:
        return 0
    elif x in d:
        return d[x]
    x_s = str(x)
    low = int('1' * len(x_s)) if int('1' * len(x_s)) <= x else int('1' * (len(x_s) - 1))
    high = int('1' * len(x_s)) if int('1' * len(x_s)) >= x else int('1' * (len(x_s) + 1))
    (l_val, h_val) = (-1, -1)
    if abs(x - low) < x:
        l_val = len(str(low)) + count(abs(x - low))
    if abs(x - high) < x:
        h_val = len(str(high)) + count(abs(x - high))
    ret = min(l_val, h_val) if min(l_val, h_val) >= 0 else max(l_val, h_val)
    d[x] = ret
    return ret


print(count(n))
