k = int(input())


def snuke(n):
    s = sum(map(int, str(n)))
    return n / s


digit = 0
ans = 1
for _ in range(k):
    print(ans)
    if snuke(ans + 10 ** digit) > snuke(ans + 10 ** (digit + 1)):
        digit += 1
    ans += 10 ** digit
