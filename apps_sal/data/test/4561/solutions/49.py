x, a, b = map(int, input().split())

if a >= b:
    print("delicious")
elif b > (x + a):
    print("dangerous")
else:
    print("safe")
