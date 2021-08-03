N = int(input())


def S(n):
    result = 0
    for i in range(len(str(n))):
        result += int(str(n)[i])
    return result


if N % S(N) == 0:
    print('Yes')
else:
    print('No')
