(a, b, x) = list(map(int, input().split()))
a_x = a // x
b_x = b // x
if a % x == 0:
    print(b_x - a_x + 1)
else:
    print(b_x - a_x)
