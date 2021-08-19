x = int(input())
m = 100
cnt = 0
while m < x:
    m += m // 100
    cnt += 1
print(cnt)
