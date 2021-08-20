def resolve():
    (a, b) = map(int, input().split())
    for i in range(20100):
        ans = '-1'
        if i * 0.08 // 1 == a and i * 0.1 // 1 == b:
            ans = i
            break
    print(ans)


resolve()
