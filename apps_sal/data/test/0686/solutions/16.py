for _ in range(int(input())):
    a, b = map(int, input().split())
    if a - b != 1:
        print("YES")
    else:
        print("NO")
