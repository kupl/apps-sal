mod = int(1000000000.0 + 7)
maxN = int(200000.0 + 100)
pow = [1] * maxN
cost = []


def add(x, y):
    return (x + y) % mod


def mul(x, y):
    return x % mod * (y % mod) % mod


def prepare():
    for i in range(1, maxN):
        pow[i] = mul(pow[i - 1], 2)


prepare()
n = int(input())
inp = input().split()
for i in range(0, n):
    cost.append(int(inp[i]))
cost.sort()
ans = 0
for i in range(1, n + 1):
    cur = mul(pow[i - 1], mul(int(cost[i - 1]), pow[n - i]))
    if i < n:
        cur = add(cur, pow[i - 1] * pow[n - i - 1] % mod * int(cost[i - 1]) % mod * (n - i) % mod)
    ans = add(ans, cur)
print(mul(ans, pow[n]))
' test\n6\n623 77 177 26 865 192\n'
