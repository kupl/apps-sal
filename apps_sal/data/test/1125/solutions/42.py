n = int(input())
A = list(map(int, input().split()))
a = A[0]
b = A[1]
x = 0
for i in A[2:]:
    x ^= i
d = {}


def F(a, b, xor):
    if (a, b, xor) in d:
        return d[a, b, xor]
    if a & 1 ^ b & 1 != xor & 1:
        return float('INF')
    if xor == 0:
        if a < b:
            return float('INF')
        else:
            return (a - b) // 2
    c1 = 2 * F(a // 2, b // 2, xor // 2)
    c2 = 2 * F((a - 1) // 2, (b + 1) // 2, xor // 2) + 1
    f = min(c1, c2)
    d[a, b, xor] = f
    return f


ans = F(a, b, x)
if ans >= a:
    print(-1)
else:
    print(ans)
