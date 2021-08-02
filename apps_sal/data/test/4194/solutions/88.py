a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
x = a[0] - sum(b)
if x < 0:
    print((-1))
else:
    print(x)
