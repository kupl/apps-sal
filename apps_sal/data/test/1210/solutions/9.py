n, p = list(map(int, input().split()))


def count_divisors(a, b, p):
    x = b // p
    y = (a - 1) // p
    return x - y


arr = []

for i in range(n):
    a, b = list(map(int, input().split()))
    arr.append((count_divisors(a, b, p), b - a + 1))

ans = 0

for i in range(n - 1):
    a, b = arr[i][0], arr[i + 1][0]
    x, y = arr[i][1], arr[i + 1][1]
    ans += 1 - ((1 - a / x) * (1 - b / y))

a, b = arr[0][0], arr[-1][0]
x, y = arr[0][1], arr[-1][1]
ans += 1 - ((1 - a / x) * (1 - b / y))

# print(ans)

print(ans * 2000)
