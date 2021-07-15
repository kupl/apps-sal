a, b, c, d = list(map(int, input().split()))
if a + b > c + d:
    print("Left")
elif a + b == c + d:
    print("Balanced")
else:
    print("Right")

