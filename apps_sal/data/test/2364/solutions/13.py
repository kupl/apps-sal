mod = 998244353


def calc(nn, costs):
    total = costs[-1]
    mult = 1
    for a in range(nn - 1, 0, -1):
        total = (total + costs[a - (nn + 1)] * mult % mod * (nn - a + 2) % mod) % mod
        mult = mult * 2 % mod
    return total


print(calc(int(input()), list(map(int, input().split(' ')))))
