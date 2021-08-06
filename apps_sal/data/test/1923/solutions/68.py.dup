N = int(input())
L = map(int, input().split())


def skewer(input):
    x = sorted(input, reverse=True)
    result = 0
    for i in range(0, len(x)):
        if i % 2 == 1:
            result = result + x[i]
    return result


print(skewer(L))
