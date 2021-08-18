k = int(input())

if k % 2 == 0 or k % 5 == 0:
    print(-1)
    return

cnt = num = 0
while 1:
    num += 7 * pow(10, cnt, k)
    num %= k
    cnt += 1
    if num == 0:
        break
print(cnt)
