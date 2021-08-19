3


def readln():
    return tuple(map(int, input().split()))


mem = dict()


def calc(a, b):
    if a == b:
        return 0
    if (a, b) in mem:
        return mem[a, b]
    var = [2 ** 30]
    if a % 2 == 0:
        var.append(calc(a // 2, b))
    if a % 3 == 0:
        var.append(calc(a // 3, b))
    if a % 5 == 0:
        var.append(calc(a // 5, b))
    if b % 2 == 0:
        var.append(calc(a, b // 2))
    if b % 3 == 0:
        var.append(calc(a, b // 3))
    if b % 5 == 0:
        var.append(calc(a, b // 5))
    mem[a, b] = min(var) + (min(var) < 2 ** 30)
    return mem[a, b]


(a, b) = readln()
res = calc(a, b)
print(-1 if res == 2 ** 30 else res)
