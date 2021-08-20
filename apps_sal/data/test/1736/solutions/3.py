(n, t) = [int(x) for x in input().split()]
minutes = [int(x) for x in input().split()]
s = 0
result = 0
left = 0
right = 0
while left < n:
    while right < n and s + minutes[right] <= t:
        s += minutes[right]
        right += 1
    result = max(result, right - left)
    s -= minutes[left]
    left += 1
print('%d' % result)
