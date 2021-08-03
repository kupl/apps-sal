n, x1, x2 = [int(i) for i in input().split()]
a = input().split()
a = a[:x1 - 1] + a[x2:]
b = input().split()
b = b[:x1 - 1] + b[x2:]
check = True
for i in range(len(a)):
    if (a[i] != b[i]):
        check = False
        break
if (check):
    print("TRUTH")
else:
    print("LIE")
