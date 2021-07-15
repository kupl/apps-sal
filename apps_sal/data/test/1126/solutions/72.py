N, X, M = map(int, input().split())

checked_val = [0] * M
sum_list = [X]
a = X

def calc_ans(sum_list, start_idx, end_idx):
    loop_len = end_idx - start_idx + 1
    loop_times = (N - start_idx - 1) // loop_len
    add = N - (loop_len * loop_times) - start_idx
    return ((sum_list[end_idx] - sum_list[start_idx - 1]) * loop_times + sum_list[start_idx - 1 + add])

for i in range(1, N):
    a = (a ** 2) % M
    if checked_val[a - 1] != 0:
        ans = calc_ans(sum_list, checked_val[a - 1], i - 1)
        break
    elif a == 0:
        ans = sum_list[i - 1]
        break
    else:
        checked_val[a - 1] = i
        sum_list.append(sum_list[-1] + a)
else:
    ans = sum_list[-1]
print(ans)
