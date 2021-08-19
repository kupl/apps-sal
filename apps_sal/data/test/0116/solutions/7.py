(l_1, r_1, l_2, r_2, k) = map(int, input().split())
left = max(l_1, l_2)
right = min(r_1, r_2)
if left > right:
    print(0)
elif left <= k <= right:
    print(right - left)
else:
    print(right - left + 1)
