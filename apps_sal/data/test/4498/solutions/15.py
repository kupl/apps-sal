def resolve():
    a, b, c, d = map(int, input().split())
    ans = ""
    if abs(c-a) <= d: ans = "Yes"
    elif abs(c-b) <= d and abs(b-a) <= d: ans = "Yes"
    else: ans = "No"
    print(ans)
resolve()
