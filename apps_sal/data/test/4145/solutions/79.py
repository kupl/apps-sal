import math


def check(n):
    p_list = []
    s_list = [*range(2, n + 1)]
    while True:
        if s_list[0] > math.sqrt(n):
            p_list.extend(s_list)
            break
        else:
            h_num = s_list[0]
            p_list.append(h_num)
            s_list.pop(0)
            s_list = [i for i in s_list if i % h_num != 0]
    return p_list


n = int(input())
s = 10 ** len(str(n))
m = sorted((i for i in check(n + s) if i >= n))
print(m[0])
