H = int(input())

cnt = 0
num = 1
while H >= 1:
    H = H // 2
    cnt += num
    num = num * 2

print(cnt)
