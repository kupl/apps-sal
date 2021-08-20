n = int(input())
s_lst = [int(input()) for _ in range(n)]
maximum = sum(s_lst)
s_lst.sort()
if maximum % 10 != 0:
    answer = maximum
else:
    for i in range(n):
        maximum -= s_lst[i]
        if maximum % 10 != 0:
            answer = maximum
            break
        else:
            maximum += s_lst[i]
        if i == n - 1 and maximum == sum(s_lst):
            answer = 0
print(answer)
