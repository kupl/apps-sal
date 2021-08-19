from collections import deque
d = deque(input())
n = int(input())
p = []
flg = 0
for i in range(n):
    p = list(input().split())
    # print(p)
    if p[0] == "1":
        flg ^= 1  # flg == 1 の場合は左右反転
        # print(flg)
    else:
        if p[1] == "1":  # 1の場合は先頭
            if flg == 1:  # 1の場合は反転
                d.append(p[2])
            else:
                d.appendleft(p[2])  # 左から入れる
        else:
            if flg == 1:
                d.appendleft(p[2])  # 左から入れる
            else:
                d.append(p[2])

if flg == 1:
    d.reverse()
a = ""
for i in d:
    a += i
print(a)
