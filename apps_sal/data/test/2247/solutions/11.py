for _ in range(int(input())):
    s, a, b, c = map(int, input().split())
    buy = s // c
    print(buy + (buy // a) * b)
