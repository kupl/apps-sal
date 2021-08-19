import math
(n, h, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
current_height = 0
seconds_past = 0
i = 0
while i < len(a):
    if current_height + a[i] <= h:
        current_height += a[i]
        i += 1
    elif current_height <= k:
        current_height = 0
        seconds_past += 1
    else:
        seconds_past += current_height // k
        current_height = current_height % k
seconds_past += math.ceil(current_height / k)
print(seconds_past)
