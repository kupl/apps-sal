n, k = map(int, input().split())
x = list(map(int, input().split()))
neg_num = n

for i in range(n):
    if x[i] > 0:
        neg_num = i
        break
pos_num = n - neg_num

l = min(k, neg_num)
res = 10 ** 13
for i in range(l, -1, -1):
    r = k - i
    if r <= pos_num:
        l_val = min(0, x[neg_num - i])
        r_val = max(0, x[neg_num + k - i - 1])
        tmp = min( -l_val * 2 + r_val, -l_val + r_val * 2)
        res = min(tmp, res)
print(res)
