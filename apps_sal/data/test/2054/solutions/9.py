for _ in range(int(input())):
    a,b = list(map(int, input().split()))
    if a < b:
        a, b = b, a
    ans = min(a - b, b)
    a -= ans * 2
    b -= ans
    if b != 0:
        ans += (a+b) // 3
    print(ans)

