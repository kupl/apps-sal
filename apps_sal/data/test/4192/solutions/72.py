num = list(map(int, input().split()))
d = num[0]
speed = num[1]
limit_t = num[2]
time = d / speed
if time <= limit_t:
    print('Yes')
else:
    print('No')
