a, b, x = [int(x) for x in input().split()]


b_num = b // x
a_num = (a - 1) // x if a - 1 >= 0 else -1
print((b_num - a_num))
