t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    if a >= 2 * b:
        print(b)
    elif b >= 2 * a:
        print(a)
    else:
        print(int((a + b) / 3))
