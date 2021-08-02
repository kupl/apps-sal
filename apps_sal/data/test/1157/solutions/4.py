n = int(input())
a = list(map(int, input().split()))

ans_pos = 0
ans_neg = 0
tmp_pos = 0
tmp_neg = 0
for i in range(n)[::-1]:
    prev_pos = tmp_pos
    prev_neg = tmp_neg
    tmp_pos = 0
    tmp_neg = 0
    if a[i] > 0:
        tmp_pos += 1
        tmp_pos += prev_pos
        tmp_neg += prev_neg
    else:
        tmp_neg += 1
        tmp_pos += prev_neg
        tmp_neg += prev_pos
    ans_pos += tmp_pos
    ans_neg += tmp_neg
print(ans_neg, ans_pos)
