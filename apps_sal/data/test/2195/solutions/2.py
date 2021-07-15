for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    a, b = list(map(int, input().split()))
    ans = a * abs(x - y)
    if a * 2 < b:
        ans += min(x, y) * a * 2
    else:
        ans += min(x, y) * b
    print(ans)
