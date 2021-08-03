import sys

l, r = tuple(int(x) for x in sys.stdin.readline().split())
maximum = -1
cur_pow = 1

while cur_pow <= r:
    if cur_pow - 1 >= l:
        cur_result = cur_pow ^ (cur_pow - 1)
        maximum = max(maximum, cur_result)
    cur_pow *= 2

if maximum < 0:
    n_ones = len(bin(l))
    str1, str2 = bin(l), bin(r)
    index = 0
    while index < len(str1) and index < len(str2) and str1[index] == str2[index]:
        index += 1
        n_ones -= 1
    if n_ones == 0:
        maximum = 0
    else:
        maximum = int('1' * n_ones, 2)

print(maximum)
