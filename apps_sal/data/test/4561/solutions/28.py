a, b, c = map(int, input().split(" "))
if c > a + b:
    print("dangerous")
elif c > a:
    print("safe")
else:
    print("delicious")
