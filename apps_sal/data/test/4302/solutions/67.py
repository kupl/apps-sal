(a, b) = map(int, input().split())
if a < b:
    (a, b) = (b, a)
if a == b:
    print(a * 2)
else:
    print(a + a - 1)
