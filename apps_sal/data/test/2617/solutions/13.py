import math


def process_test_case(i_test):
    n = int(input())
    n_days = math.floor(math.log2(n))
    out_list = []
    n_threshold = int(pow(2, n_days) + pow(2, n_days - 1) - 1)
    if n >= n_threshold:
        for i in range(n_days - 1):
            out_list.append(str(int(pow(2, i))))
        out_list.append(str(int(n - n_threshold)))
    else:
        for i in range(n_days - 2):
            out_list.append(str(int(pow(2, i))))
        n_reminder = n - pow(2, n_days) + 1
        a = n_reminder // 2
        b = n_reminder - 2 * a
        out_list.append(str(a))
        out_list.append(str(b))
    print(int(n_days))
    print(' '.join(out_list))


n_tests = int(input())
for i_test in range(1, n_tests + 1):
    process_test_case(i_test)
