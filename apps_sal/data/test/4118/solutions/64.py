(a, b) = input().split()
a1 = len(a)
b1 = len(b)
if a1 > 1 or b1 > 1:
    print(-1)
else:
    print(int(a) * int(b))
