s = list(input())

k = int(input())

cnt = 0
ans = 0
for i in s:
    if int(i) == 1:
        cnt += 1
        continue

    else:
        ans += int(i)
        break

if k <= cnt:
    print((1))

else:
    print(ans)
