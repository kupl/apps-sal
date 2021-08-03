INF = 10**18


def calc(a, b, xor):
    if (a, b, xor) in memo:
        return memo[(a, b, xor)]
    if (a & 1) ^ (b & 1) != (xor & 1):
        return INF
    if xor == 0:
        if a < b:
            return INF
        else:
            return (a - b) // 2
    x = 2 * calc(a // 2, b // 2, xor // 2)
    y = 2 * calc((a - 1) // 2, (b + 1) // 2, xor // 2) + 1
    memo[(a, b, xor)] = min(x, y)
    return memo[(a, b, xor)]


n = int(input())
arr = list(map(int, input().split()))
a, b = arr[0], arr[1]
xor = 0
for i in range(2, n):
    xor ^= arr[i]
memo = {}
ans = calc(a, b, xor)
if ans >= a:
    print(-1)
else:
    print(ans)
