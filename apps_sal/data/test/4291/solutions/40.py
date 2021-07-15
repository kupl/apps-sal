from itertools import accumulate

n, q = list(map(int, input().split()))
s = input()
lr = [list(map(int, input().split())) for _ in range(q)]

ac_list = [0]*n

for i in range(n-1):
    if s[i] == 'A' and s[i+1] == 'C':
        ac_list[i] = 1

ac_sum = list(accumulate(ac_list))

for l, r in lr:
    l -= 1
    r -= 1
    if l == 0:
        print((ac_sum[r-1]))
        continue
    print((ac_sum[r-1] - ac_sum[l-1]))

