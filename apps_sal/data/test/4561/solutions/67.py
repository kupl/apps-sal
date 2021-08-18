X, A, B = [int(v) for v in input().split(" ")]


result = A - B

if result >= 0:
    print("delicious")
elif abs(result) > X:
    print("dangerous")
else:
    print("safe")
