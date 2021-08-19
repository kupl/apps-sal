k = int(input())


def make_lunlun(lunlun_lst):
    ret_lunlun = []
    for num in lunlun_lst:
        num_str = str(num)
        if num_str[-1] != '0':
            num_tmp = num_str + str(int(num_str[-1]) - 1)
            ret_lunlun.append(int(num_tmp))
        if num_str[-1] != '9':
            num_tmp = num_str + str(int(num_str[-1]) + 1)
            ret_lunlun.append(int(num_tmp))
        num_tmp = num_str + num_str[-1]
        ret_lunlun.append(int(num_tmp))
    return ret_lunlun


lunlun_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while 1:
    if len(lunlun_lst) < k:
        k -= len(lunlun_lst)
        lunlun_lst = make_lunlun(lunlun_lst)
    else:
        lunlun_lst.sort()
        print(lunlun_lst[k - 1])
        break
