# 105の約数は1, 3, 5, 7, 3 * 5, 3 * 7, 5 * 7, 3 * 5 * 7
# ほかにありえるのは
# ①1, 3, 5, 9, ...
# ②1, 3, 5, 11, ...
# ③1, 3, 7, 9, ...
# ④1, 3, 5, 13, ...
n = int(input())
if n < 105:
    print(0)
elif n < 135:
    print(1)
elif n < 165:
    print(2)
elif n < 189:
    print(3)
elif n < 195:
    print(4)
else:
    print(5)
