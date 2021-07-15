for __ in range(int(input())):
    a, b = list(map(int, input().split()))
    print(24 * 60 - a * 60 - b)
