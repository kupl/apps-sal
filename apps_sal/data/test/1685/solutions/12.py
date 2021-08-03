def powersOfTwo():
    powers = {}
    powers[0] = 1
    for i in range(1, 70):
        powers[i] = powers[i - 1] * 2
    return powers


def log2(num):
    ans = 0
    while num > 1:
        num //= 2
        ans += 1
    return ans


def getlevel(num):
    count = 0
    while num % 2 == 0:
        num //= 2
        count += 1
    return count


def solve():
    n, q = list(map(int, input().rstrip().split()))
    powers = powersOfTwo()
    maxlevel = log2(n + 1) - 1
    for _ in range(q):
        num = int(input().rstrip())
        level = getlevel(num)
        string = input().rstrip()
        for char in string:
            assert 0 <= level <= maxlevel
            if char == 'U':
                if level < maxlevel:
                    a = num - powers[level]
                    b = num + powers[level]
                    if a == 0:
                        num = b
                    elif b > n:
                        num = a
                    elif getlevel(a) < getlevel(b):
                        num = a
                    else:
                        num = b
                    level += 1
            elif char == 'L':
                if level > 0:
                    num -= powers[level - 1]
                    level -= 1
            elif char == 'R':
                if level > 0:
                    num += powers[level - 1]
                    level -= 1
            else:
                raise ValueError
        print(num)


def __starting_point():
    solve()


__starting_point()
