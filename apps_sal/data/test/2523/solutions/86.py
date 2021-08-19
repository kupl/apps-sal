slist = list(map(int, list(input())))
len_s = len(slist)

min_answer = len_s
for i in range(1, len_s):
    if slist[i - 1] != slist[i]:
        min_answer = min(min_answer, max(i, len_s - i))
        # print(i,len(slist)-i)

print(min_answer)
