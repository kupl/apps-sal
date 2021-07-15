def count_unic_mess(crt, display, array, n, result_arr):
    low_bound = 0 if crt - display < 0 else crt - display

    high_bound = n if crt + display + 1 > n else crt + display + 1

    result = high_bound - low_bound

    if array[crt] == 0:
        result_arr.append(result)
        return result

    ref = array[crt] - 1
    high_bound_ref = n if ref + display + 1 > n else ref + display + 1

    if high_bound_ref >= low_bound:
        result += result_arr[ref] - high_bound_ref + low_bound
    else:
        result += result_arr[ref]

    result_arr.append(result)
    return result


n, k = map(int, input().split(' '))

links = [int(x) for x in input().split(' ')]
count_arr = []

for i in range(n):
    print(count_unic_mess(i, k, links, n, count_arr), end=' ')

