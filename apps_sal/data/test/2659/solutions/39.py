K = int(input())


def snuke(n):
    n_list = [int(i) for i in list(str(n))]
    return n / sum(n_list)


ans = 1
digit = 0

while K > 0:
    print(ans)
    if snuke(ans + 10**digit) > snuke(ans + 10**(digit + 1)):
        digit += 1
    ans += 10**digit
    K -= 1
