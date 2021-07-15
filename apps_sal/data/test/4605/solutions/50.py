n_num, a_num, b_num = map(int, input().split())

def digit_sum(num):
    str_num = str(num)
    digit_num = 0
    for s in str_num:
        digit_num += int(s)
    return digit_num

cnt = 0
for n in range(1, n_num+1):
    if a_num <= digit_sum(n) <= b_num:

        cnt += n
        
print(cnt)
