import math
import bisect


def get_prime(number):
    prime_list = []
    search_list = list(range(2, number + 1))
    while search_list[0] <= math.sqrt(number):
        head_num = search_list.pop(0)
        prime_list.append(head_num)
        search_list = [num for num in search_list if num % head_num != 0]
    prime_list.extend(search_list)
    return prime_list


l = get_prime(100000)
l2 = []
for i in range(len(l)):
    x = l[i]
    y = (x + 1) // 2
    if y in l:
        l2.append(x)

Q = int(input())
for i in range(Q):
    a, b = list(map(int, input().split()))
    x = bisect.bisect_left(l2, a)
    y = bisect.bisect_right(l2, b)
    print((y - x))
