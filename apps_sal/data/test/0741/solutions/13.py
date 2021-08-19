(n, m) = list(map(int, input().split()))
tm = [int(i) for i in input().split()]
sum_d = 0
sum_l = 0
is_dark = n & 1
lst = m
tm.reverse()
tm.append(0)
Max = -1
for i in tm:
    dis = lst - i
    if is_dark:
        sum_d += dis
    else:
        sum_l += dis
    lst = i
    if dis == 1:
        is_dark ^= 1
        continue
    if is_dark:
        fake_l = sum_d - 1
    else:
        fake_l = sum_d + dis - 1
    is_dark ^= 1
    Max = max(Max, fake_l - sum_l)
ans = sum_l
if Max > 0:
    ans += Max
print(ans)
