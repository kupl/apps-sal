a, b = map(int, input().split())


def ans086(a: int, b: int):
    ab = int(str(a) + str(b))
    import math
    if int(math.sqrt(ab))**2 == ab:
        return("Yes")
    else:
        return("No")


print(ans086(a, b))
