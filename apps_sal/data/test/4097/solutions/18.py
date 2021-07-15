n = int(input())
ans = 200000
a = list(map(int, input().split()))

def test(x, y):
    if ((a[n - 1] + y) - (a[0] + x)) % (n - 1):
        return False
    first = a[0] + x
    last = a[n - 1] + y
    d = (last - first) // (n - 1)
    for i in range(1, n - 1):
        if abs((first + i * d) - a[i]) > 1:
            return False
    return True

def find(x, y):
    res = abs(x) + abs(y)
    first = a[0] + x
    last = a[n - 1] + y
    d = (last - first) // (n - 1)
    for i in range(1, n - 1):
        if abs((first + i * d) - a[i]):
            res += 1
    return res

if n <= 2:
    print(0)
else:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if test(i, j):
                ans = min(ans, find(i, j))
    print(-1 if ans == 200000 else ans)
