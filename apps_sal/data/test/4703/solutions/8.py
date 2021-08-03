s = input()
len_s = len(s)

total = int(s)
eval_s = ""
insert_list = []
for i in range(1, 2 ** (len_s - 1)):
    # print(i)
    for j in range(len_s):
        eval_s += s[j]
        if ((i >> j) & 1):
            # print(i, j)
            eval_s += "+"
    # print(eval_s)
    total += eval(eval_s)
    eval_s = ""
print(total)
