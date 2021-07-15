
digit_set = set(range(10))
double_digit_set = set(range(19))
A = [int(i) for i in input()]
first_sum = sum(A[:3])
second_sum = sum(A[3:])
one_flag = True
exit_flag = False
if first_sum == second_sum:
    print(0)
else:
    for i in range(6):
        if i < 3:
            if second_sum - (first_sum - A[i]) in digit_set:
                print(1)
                one_flag = False
                break
        else:
            if first_sum - (second_sum - A[i]) in digit_set:
                print(1)
                one_flag = False
                break
    if one_flag:
        for i in range(6):
            for j in range(i+1, 6):
                if i < 3 and j < 3:
                    if second_sum - (first_sum - A[i] - A[j]) in double_digit_set:
                        print(2)
                        exit_flag = True
                        break
                if i >= 3 and j >= 3:
                    if first_sum - (second_sum - A[i] - A[j]) in double_digit_set:
                        print(2)
                        exit_flag = True
                        break
                elif abs(first_sum - A[i] - second_sum + A[j]) <= 9:
                    print(2)
                    exit_flag = True
                    break
            if exit_flag:
                break
        else:
            print(3)






