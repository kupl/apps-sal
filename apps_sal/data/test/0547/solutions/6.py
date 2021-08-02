n, k = (int(i) for i in input().split())
l = []
for i in range(n):
    l += [input()]
ans_pas = input()
low_bow = 0
up_bow = 0
for el in l:
    if len(el) < len(ans_pas):
        low_bow += 1
    elif len(el) == len(ans_pas):
        up_bow += 1
up_bow += low_bow - 1
min_ans = low_bow + (low_bow // k) * 5 + 1
max_ans = up_bow + (up_bow // k) * 5 + 1
print(min_ans, max_ans)
