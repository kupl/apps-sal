k = int(input().strip())
n = k % 4
if k == 0:
    print(1)
elif n == 0:
    print(6)
elif n == 1:
    print(8)
elif n == 2:
    print(4)
else:
    print(2)
