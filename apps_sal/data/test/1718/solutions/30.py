n, k = list(map(int, input().split()))
lis = list(map(int, input().split()))
left = 0
if n == k:
    print((1))
    return
if (n // 2) < k:
    print((2))
    return
for i in range(n):
    if lis[i] == 1:
        break
    else:
        left += 1
right = n - left - 1
k = k - 1
left_ans = 0
right_ans = 0
if left % k == 0:
    left_ans += (left // k)
    if right % k == 0:
        left_ans += (right // k)
    else:
        left_ans += ((right // k) + 1)
else:
    left_ans += ((left // k) + 1)
    right_tmp = right - (k - (left % k))
    if right_tmp % k == 0:
        left_ans += (right_tmp // k)
    else:
        left_ans += ((right_tmp // k) + 1)

if right % k == 0:
    right_ans += (right // k)
    if left % k == 0:
        right_ans += (left // k)
    else:
        right_ans += ((left // k) + 1)
else:
    right_ans += ((right // k) + 1)
    left_tmp = left - (k - (right % k))
    if left_tmp < 1:
        pass
    elif left_tmp % k == 0:
        right_ans += (left_tmp // k)
    else:
        right_ans += ((left_tmp // k) + 1)
print((min(left_ans, right_ans)))
