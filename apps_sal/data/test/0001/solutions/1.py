s_num = input()
num = int(s_num)
digs = [int(s_num[i]) for i in range(len(s_num))]

max_sum = sum(digs)
res = num
for i in range(len(s_num)):
    if (digs[i] != 0):
        digs[i] -= 1
        n_sum = sum(digs[:i + 1]) + 9 * (len(s_num) - i - 1)
        if n_sum >= max_sum:
            n_res = int(''.join([str(digs[i]) for i in range(i + 1)]) + '9' * (len(s_num) - i - 1))
            if (n_sum == max_sum):
                res = max(n_res, res)
            else:
                res = n_res
            max_sum = n_sum

        digs[i] += 1
print(res)
