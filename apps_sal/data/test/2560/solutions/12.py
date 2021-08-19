import sys
sys.setrecursionlimit(1500)
inst_num = int(input())
n = 0
l = 0
r = 0


def payment_possible(total, l, r):
    max_coins = int(total / l)
    if r * max_coins >= total:
        return True
    else:
        return False
    if total < coins[0]:
        return False
    return False


for i in range(0, inst_num):
    line_data = input().split()
    n = int(line_data[0])
    l = int(line_data[1])
    r = int(line_data[2])
    if n > 0 and l == 1:
        print('Yes')
        continue
    if n >= l and n <= r:
        print('Yes')
        continue
    if payment_possible(n, l, r):
        print('Yes')
    else:
        print('No')
'\n    if sum > 0 and l == 1:\n        return True\n    if sum >= l and sum <= r:\n        return True\n    if sum == 0:\n        return True\n    if sum > 0 and r < l:\n        return False\n\n    new_sum = sum - (r * int(sum / r))\n    print(new_sum, r)\n    r -= 1\n    return payment_possible(new_sum, l, r)\n'
