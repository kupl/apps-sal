n = int(input())
data = [int(i) for i in input().split()]
box = []
l = 0
for i in range(n):
    if data[i] == 1:
        box.append(i)
        l += 1
if l:
    ret = 1
    for i in range(l - 1, 0, -1):
        ret *= box[i] - box[i - 1]
    print(ret)
else:
    print(0)
