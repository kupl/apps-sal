import sys
ilist = [int(i) for i in input().split()]
(n, k) = (ilist[0], ilist[1])
a = [int(i) for i in input().split()]
(left, right) = ([], [])
for i in range(n):
    left.append(i - 1)
    right.append(i + 1)
val_idx = [[a[i], i] for i in range(n)]
val_idx = sorted(val_idx, key=lambda x: x[0], reverse=True)
result = [0 for i in range(n)]
finished = 0
team = 1
for (val, idx) in val_idx:
    if finished == n:
        break
    if result[idx] != 0:
        continue
    result[idx] = team
    finished += 1
    left_k = k
    most_left = left[idx]
    while left_k > 0 and most_left >= 0:
        result[most_left] = team
        finished += 1
        most_left = left[most_left]
        left_k -= 1
    right_k = k
    most_right = right[idx]
    while right_k > 0 and most_right < n:
        result[most_right] = team
        finished += 1
        most_right = right[most_right]
        right_k -= 1
    if most_left >= 0:
        right[most_left] = most_right
    if most_right < n:
        left[most_right] = most_left
    if team == 1:
        team = 2
    else:
        team = 1
print(''.join([str(i) for i in result]))
