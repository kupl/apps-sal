def resolve():
    s, p = map(int, input().split())
    for i in range(1000002):
        if (s - i) * i == p:
            print("Yes")
            return
    else:
        print("No")


resolve()
