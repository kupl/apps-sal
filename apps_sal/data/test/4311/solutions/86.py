s = int(input())


def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


x = set()
ans = 0
while True:
    ans += 1
    if s in x:
        print(ans)
        break
    x.add(s)
    s = f(s)
