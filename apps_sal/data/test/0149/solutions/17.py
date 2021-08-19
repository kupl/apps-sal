[x, y, l, r] = list(map(int, input().rstrip().split()))
data = [l]
lbad = False
rbad = False
for i in range(0, 61):
    for j in range(0, 61):
        num = x ** i + y ** j
        if num == l:
            lbad = True
        if num == r:
            rbad = True
        if l <= num <= r:
            data.append(num)
        elif num > r:
            break
data.sort()
max_time = 0
data.append(r if rbad else r + 1)
data[0] = l if lbad else l - 1
for i in range(0, len(data) - 1):
    max_time = max(data[i + 1] - data[i] - 1, max_time)
print(max_time)
