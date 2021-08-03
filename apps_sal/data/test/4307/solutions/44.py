in_num = int(input())
check_num = 1
ans_counter = 0


while check_num <= in_num:
    i = 1
    div_counter = 0
    while i <= check_num:
        if check_num % i == 0:
            div_counter += 1
        i += 2
    if div_counter == 8:
        ans_counter += 1
    check_num += 2

print(ans_counter)
