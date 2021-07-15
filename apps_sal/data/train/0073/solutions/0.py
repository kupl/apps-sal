def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * (n + 1)
    def inc():
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                return False
        return True
    def calc():
        for i in range(n + 1):
            c[i] = 0
        for i in a:
            c[i] += 1
        for i in range(n + 1):
            if not c[i]:
                return i
        return n + 1
    ans = []
    while not inc():
        x = calc()
        if x >= n:
            y = 0
            while y < n and a[y] == y:
                y += 1
            a[y] = x
            ans.append(y)
        else:
            a[x] = x
            ans.append(x)
    print(len(ans))
    print(*map(lambda x: x + 1, ans))

t = int(input())
for _ in range(t):
    solve()
