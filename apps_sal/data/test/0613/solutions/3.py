def main():
    (t, a, b) = list(map(int, input().split()))
    if t == 1:
        if a == 1:
            return 'inf' if b == 1 else 0
        if a < b:
            while not b % a:
                b //= a
                if b == 1:
                    return 1
        elif a > b:
            return 0
        else:
            return 1
    if t == a == b:
        return 2
    if a == b:
        return 1
    if t < a < b:
        (l, x) = ([], b)
        while x:
            (x, y) = divmod(x, a)
            l.append(y)
        x = 0
        for c in reversed(l):
            x = x * t + c
        return 1 if x == a else 0
    if t == a != b or t > a or a > b:
        return 0
    return 1


print(main())
