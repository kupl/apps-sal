import sys
import os
import math
(n, f) = map(int, input().split())
A = []
normal_sell_total = 0
for i in range(n):
    (product_num, client_num) = map(int, input().split())
    if product_num >= client_num:
        normal_sell_num = client_num
    else:
        normal_sell_num = product_num
    normal_sell_total += normal_sell_num
    if product_num * 2 >= client_num:
        double_sell_num = client_num
    else:
        double_sell_num = product_num * 2
    diff = double_sell_num - normal_sell_num
    A.append(diff)
A.sort(reverse=True)
increased_sell_num = sum(A[:f])
print(normal_sell_total + increased_sell_num)
