k = int(input())
a, b = list(map(int, input().split()))

t = b // k
u = (a - 1) // k

if t - u >= 1:
    print("OK")
else:
    print("NG")
