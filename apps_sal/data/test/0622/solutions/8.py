def p(n, k):
    if k == 2 ** (n - 1):
        return(n)
    if k > 2 ** (n - 1):
        k -= 2 ** (n - 1)
    return p(n - 1, k)

n, k = map(int, input().split())
print(p(n, k))
