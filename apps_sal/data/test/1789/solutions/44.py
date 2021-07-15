def solve(a, b, x, y):
    if b < a:
        return x + (a-b-1)*min(2*x, y)
    else:
        return x + (b-a)*min(2*x, y)

a, b, x, y = list(map(int, input().split()))
print((solve(a, b, x, y)))

