a, b = map(int, input().split())


def ff(n):
    tmp = (n + 1) // 2
    tmp %= 2
    if n % 2 == 1:
        return tmp
    else:
        return n ^ tmp


ans = ff(a - 1) ^ ff(b)
print(ans)
