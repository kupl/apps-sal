n, k = list(map(int, input().split()))
num = n / k
if n < k:
    print((1))
elif num.is_integer():
    print((0))
else:
    print((1))
