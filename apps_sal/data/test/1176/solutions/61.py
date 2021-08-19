N = int(input())
A = list(map(int, input().split()))
minus_cnt = 0
for a in A:
    if a < 0:
        minus_cnt += 1
abs_A = list(map(abs, A))
sum_ = sum(abs_A)
if minus_cnt % 2 == 0:
    ans = sum_
else:
    ans = sum_ - 2 * min(abs_A)
print(ans)
