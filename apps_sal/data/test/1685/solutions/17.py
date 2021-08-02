def greatest_pow2_divisor(x):
    pow2 = 1
    while x % pow2 == 0:
        pow2 *= 2
    return pow2 // 2


def parent(x):
    pow2 = greatest_pow2_divisor(x)
    if ((x + pow2) // (pow2 * 2)) % 2 == 1:
        return x + pow2
    return x - pow2


def left(x):
    if x % 2 == 1:
        return x
    return x - greatest_pow2_divisor(x) // 2


def right(x):
    if (x % 2 == 1):
        return x;
    return x + greatest_pow2_divisor(x) // 2;


numbers = list(map(int, input().split()))
n = numbers[0]
q = numbers[1]
root = (n + 1) / 2
for i in range(q):
    u = int(input())
    s = input()
    for c in s:
        if c == 'U':
            if u != root:
                u = parent(u)
        if (c == 'L'):
            u = left(u)
        if (c == 'R'):
            u = right(u)
    print(u)
