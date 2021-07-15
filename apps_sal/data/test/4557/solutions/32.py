def resolve():
    a, b, x = map(int, input().split())
    ans = ""
    if a <= x and x <= a+b:
        ans = "YES"
    else:
        ans = "NO"
    print(ans)
resolve()
