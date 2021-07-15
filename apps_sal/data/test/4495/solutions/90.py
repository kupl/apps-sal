a,b,x = list(map(int, input().split()))

if a == 0:
    mi = -1
elif a > 1:
    mi = (a - 1) // x
else:
    mi = 0
ma = b // x if b != 0 else 0

print((ma-mi))

