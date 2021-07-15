for __ in range(int(input())):
    a, b = list(map(int, input().split()))
    if a * 2 <= b:
        print(a, 2 * a)
    else:
        print(-1, -1)
