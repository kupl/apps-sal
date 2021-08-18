s = input()
k = int(input())

l = k
count = 0
n = len(s)
lst = 'abcdefghijklmnopqrstuvwxyz'
for alpha in lst:
    alpha_index = []
    for index in range(n):
        if alpha == s[index]:
            alpha_index.append(index)
    if len(alpha_index) > 0:
        cand_lst = []
        for index2 in alpha_index:
            end_lst = [index2 + m for m in range(1, 6) if index2 + m <= n]
            for end in end_lst:
                cand_lst.append(s[index2:end])
        cand_lst = set(cand_lst)
        cand_lst = sorted(cand_lst)
        if len(cand_lst) < l:
            l = l - len(cand_lst)
        else:
            res = cand_lst[l - 1]
            break

print(res)
