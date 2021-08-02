def mymod(x, a, b):
    import math
    return x - math.ceil(int(x * a / b)) * b / a


n, a, b = map(int, input().strip().split())
x = list(map(int, input().split()))
for q in x:
    print(int(mymod(q, a, b)), end=' ')
