a, b, c, d = list(map(int, input().split()))

if a + b < c + d:
    print("Right")
elif c + d < a + b:
    print("Left")
else:
    print("Balanced")
