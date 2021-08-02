from collections import defaultdict

n, k = list(map(int, input().split()))
top = [0] * n
sub = []

for i in range(n):
    t, d = list(map(int, input().split()))
    t -= 1
    if top[t] == 0:
        top[t] = d
    else:
        if d > top[t]:
            sub.append(top[t])
            top[t] = d
        else:
            sub.append(d)

top.sort(reverse=True)
top_sum = [0]
sub.sort(reverse=True)
sub_sum = [0]

for p in top:
    if p == 0:
        top_sum.append(-1)
    else:
        top_sum.append(top_sum[-1] + p)

for p in sub:
    sub_sum.append(sub_sum[-1] + p)

ans = 0

for i in range(1, k + 1):
    if (len(sub_sum) - 1) >= (k - i) and top_sum[i] != -1:
        ans = max(ans, top_sum[i] + sub_sum[k - i] + i ** 2)

print(ans)
