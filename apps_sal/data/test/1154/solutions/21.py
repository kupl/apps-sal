(n, h, k) = list(map(int, input().split()))
ip = list(map(int, input().split()))
time = 0
count = 0
height = 0
while count < n:
    if height + ip[count] <= h:
        height += ip[count]
        count += 1
    elif height % k == 0:
        time += height // k
        height = 0
    elif height >= k:
        time += height // k
        height = height % k
    else:
        height -= min(k, height)
        time += 1
if height == 0:
    s = 0
elif height % k == 0:
    s = height // k
else:
    s = height // k + 1
print(time + s)
