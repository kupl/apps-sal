def calc(x):
    ans = 0
    n = len(x)
    for (i, a) in enumerate(x):
        ans += i * a - (n - 1 - i) * a
    return ans


(n, m) = map(int, input().split())
x = tuple(map(int, input().split()))
y = tuple(map(int, input().split()))
print(calc(x) * calc(y) % int(1000000000.0 + 7))
