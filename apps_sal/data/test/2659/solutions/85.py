k = int(input())
sunuke_list = [1, 2, 3, 4, 5, 6, 7, 8]


def s(n):
    n_charlist = list(str(n))
    return sum(list(map(int, n_charlist)))


def combine_int(i, n):
    i_charlist = list(str(i))
    n_charlist = ['9'] * n
    ret_charlist = i_charlist + n_charlist
    ret_str = ''.join(ret_charlist)
    return int(ret_str)


for n in range(1, 14):
    if n >= 12:
        i = n - 2
    else:
        i = n - 1
    while (i + 1) / (s(i) + 9 * n) <= (i + 2) / (s(i + 1) + 9 * n):
        sunuke_list.append(combine_int(i, n))
        i += 1
for i in range(k):
    print(sunuke_list[i])
