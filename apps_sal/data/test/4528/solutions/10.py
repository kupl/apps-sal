for _ in range(int(input())):
    (h, m) = list(map(int, input().split()))
    print(1440 - (h * 60 + m))
