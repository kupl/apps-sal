def resolve():
    a,b = map(int,input().split())
    cnt = 1
    ans = 0
    while cnt < b:
        cnt = cnt - 1 + a
        ans += 1
    print(ans)
resolve()
