a, b = map(int, input().split())
if a <= 5:
    print(0)
    return
elif 6 <= a <= 12:
    print(b // 2)
    return
else:
    print(b)
