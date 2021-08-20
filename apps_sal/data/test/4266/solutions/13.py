(k, x) = (int(i) for i in input().split())
list_ans = []
for i in range(0, 2 * k - 1):
    list_ans.append(str(x + i - (k - 1)))
print(' '.join(list_ans))
