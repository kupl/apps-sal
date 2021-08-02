class Info:
    def __init__(self, num, p, y, id):
        self.num = num
        self.p = p
        self.y = y
        self.id = id


n, m = map(int, input().split())
info = [Info(0, 0, 0, '')]
for num in range(1, m + 1):
    p, y = map(int, input().split())
    info.append(Info(num, p, y, ''))

info = sorted(info, key=lambda x: (x.p, x.y))

cnt = 1
for i in range(1, m + 1):
    if info[i].p != info[i - 1].p:
        cnt = 1
    else:
        cnt += 1
    info[i].id = "{0:06d}{1:06d}".format(info[i].p, cnt)

info = sorted(info, key=lambda x: x.num)
info.pop(0)

for x in info:
    print(x.id)
