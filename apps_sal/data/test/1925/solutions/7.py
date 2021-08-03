a, b, n = map(int, input().split())

if b == 1:
    print(0)
    return
else:
    x = min(b - 1, n)
    ans = (a * x) // b - a * (x // b)
print(ans)
