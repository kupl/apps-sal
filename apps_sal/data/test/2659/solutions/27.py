def sum_digit(n):
    n_str = str(n)
    ans = 0
    for dig in n_str:
        ans += int(dig)
    return ans


def snuke(n):
    return n / sum_digit(n)


K = int(input())
ans = 1
print(ans)
for i in range(K - 1):
    s = len(str(ans))
    x = snuke(ans)
    L = [[ans + 10 ** k, snuke(ans + 10 ** k)] for k in range(s + 1)]
    L.sort(key=lambda x: x[1])
    ans = L[0][0]
    print(ans)
