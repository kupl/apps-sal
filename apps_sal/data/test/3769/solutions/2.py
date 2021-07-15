q = 10 ** 9 + 7

def solve(p, k):
    if k == 0:
        return pow(p, p-1, q)
    if k == 1:
        return pow(p, p, q)
    x, y = k, 1
    while x != 1:
        x *= k
        x %= p
        y += 1

    return pow(p, (p-1)//y, q)

p, k = list(map(int, input().split()))
print(solve(p, k))

