K = int(input())
x = int(K / 2)
if K % 2 == 0:
    print(x * x)
else:
    print(x * (x + 1))
