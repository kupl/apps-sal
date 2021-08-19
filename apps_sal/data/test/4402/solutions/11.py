(a, b) = map(int, input().split())
if a > 12:
    print(b)
elif 6 <= a <= 12:
    print(b // 2)
elif 0 <= a <= 5:
    print(0)
