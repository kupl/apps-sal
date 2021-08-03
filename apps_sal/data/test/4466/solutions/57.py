X, Y, Z = [int(i) for i in input().split()]

n = X // (Y + Z)
m = X % (Y + Z)

if m >= Z:
    print(n)
else:
    print((n - 1))
