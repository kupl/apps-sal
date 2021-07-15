n = int(input())
a = list(map(int, input().split()))

def cost(a, neg=False):
    sign = -1 if neg else 1
    if sign * a[0] > 0:
        ret = 0
        cum = a[0]
    else:
        ret = abs(a[0] - sign)
        cum = sign
    for i in range(1, n):
        sign *= -1
        cum += a[i]
        if cum * sign > 0:
            continue
        else:
            ret += abs(cum - sign)
            cum = sign
    return ret

print((min(cost(a, False), cost(a, True))))

