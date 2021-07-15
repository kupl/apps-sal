h = int(input())

cnt = 0
num = 1
while h > 0:
    cnt += num
    h = h // 2
    num *= 2
print(cnt)
