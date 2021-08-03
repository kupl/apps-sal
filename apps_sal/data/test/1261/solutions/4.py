def sfy(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    elif n == 3:
        return [1, 1, 3]
    else:
        if n % 2 == 0:
            return [1] * (n // 2) + [2 * x for x in sfy(n // 2)]
        else:
            return [1] * (1 + n // 2) + [2 * x for x in sfy(n // 2)]


print(" ".join([str(x) for x in sfy(int(input()))]))
