def base3(n):
    array = []
    while n > 0:
        array.append(n % 3)
        n //= 3
    return array


def good(n):
    return 2 not in base3(n)


def convert(array):
    return sum((array[i] * 3 ** i for i in range(len(array))))


for _ in range(int(input())):
    n = base3(int(input()))
    i = 0
    for i in range(len(n) - 1, -1, -1):
        if n[i] == 2:
            for j in range(i - 1, -1, -1):
                n[j] = 0
            break
    i = 0
    while i < len(n):
        if n[i] > 2:
            if i < len(n) - 1:
                n[i + 1] += n[i] // 3
            else:
                n.append(n[i] // 3)
            n[i] %= 3
        if n[i] == 2:
            if i < len(n) - 1:
                n[i + 1] += 1
            else:
                n.append(1)
            n[i] = 0
        i += 1
    print(convert(n))
