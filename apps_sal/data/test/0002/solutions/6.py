def solve(n):
    if (n < 10):
        return 1
    a = str(n)
    b = int(a[1:])
    return 10**(len(a) - 1) - b


n = int(input())
print(solve(n))
