(a, b) = map(int, input().split())
if a * 2 <= b:
    c = (b - a * 2) // 4
    print(a + c)
if a * 2 > b:
    print(b // 2)
