(n, pos, l, r) = list(map(int, input().split()))
left_first = 10 ** 6
right_first = 10 ** 6
if l == 1 and r == n:
    left_first = 0
elif l == 1:
    if pos < r:
        right_first = r - pos + 1
    else:
        right_first = pos - r + 1
elif r == n:
    if pos < l:
        left_first = l - pos + 1
    else:
        left_first = pos - l + 1
elif pos < l:
    left_first = l - pos + 1 + r - l + 1
elif l <= pos <= r:
    left_first = pos - l + r - l + 2
    right_first = r - pos + r - l + 2
else:
    right_first = pos - r + r - l + 2
print(min([left_first, right_first]))
