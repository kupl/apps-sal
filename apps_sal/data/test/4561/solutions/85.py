a, b, c = map(int, input().split())
if b < c:
    if abs(b - c) <= a:
        print("safe")
    else:
        print("dangerous")
else:
    print("delicious")
