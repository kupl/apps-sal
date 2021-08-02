for i in range(int(input())):
    a, b, c = list(map(int, input().split()))
    if a + c <= b:
        print(0)
    else:
        print(min((a + c - b + 1) // 2, c + 1))
