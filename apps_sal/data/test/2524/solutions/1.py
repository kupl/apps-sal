n = int(input())
a = [int(i) for i in input().split()]
a_bin = []
for i in a:
    a_bin.append(format(i, '#062b')[2:])


def get_keta_num(keta, a_list):
    zero = 0
    one = 0
    for i in a_list:
        if i[-keta] == '0':
            zero += 1
        else:
            one += 1
    return zero * one


ans = 0
for i in range(1, 61):
    ans += 2 ** (i - 1) * get_keta_num(i, a_bin)
    ans = ans % (10 ** 9 + 7)
print(ans)
