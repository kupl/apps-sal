def cal(sorted_list, size):
    max_sum = 0
    for k in range(len(sorted_list)):
        max_sum = max(sorted_list[k], max_sum)
        for i in range(k + 1, size):
            temp_1 = sorted_list[i]
            if sorted_list[k] % temp_1 != 0:
                if i + 1 < size and max_sum >= sorted_list[k] + sorted_list[i] + sorted_list[i + 1]:
                    break
                check_sum = sorted_list[k] + temp_1
                max_sum = max(max_sum, check_sum)
                for j in range(i + 1, size):
                    if max_sum >= sorted_list[k] + sorted_list[i] + sorted_list[j]:
                        break
                    temp_2 = sorted_list[j]
                    if sorted_list[k] % temp_2 != 0 and temp_1 % temp_2 != 0:
                        max_sum = max(max_sum, check_sum + temp_2)
                        break
    return max_sum


def solve():
    no_querries = int(input())
    output = []
    for i in range(no_querries):
        size = int(input())
        alist_raw = input().split()
        alist = [int(x) for x in alist_raw]
        alist.sort(reverse=True)
        alist = unique(alist)
        output.append(cal(alist, len(alist)))
    for x in output:
        print(x)


def unique(alist):
    unique = [alist[0]]
    for i in range(1, len(alist)):
        if alist[i] < unique[len(unique) - 1]:
            unique.append(alist[i])
    return unique


solve()
