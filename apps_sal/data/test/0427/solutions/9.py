c1, c2, x, y = list(map(int, input().split()))
def get(n):
    if (n - n // (x * y)) >= c1 + c2 and (n - n // x >= c1) and (n - n // y >= c2):
        return True
    else:
        return False
l = 0
r = c1 * x + c2 * y
while (r - l > 1):
    m = (l + r) // 2
    if get(m):
        r = m
    else:
        l = m
print(r)

