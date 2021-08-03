s = list(map(int, input()))
cur = len(s) - 1
x = True
tmp = 0
ans = 0

while cur >= 0:
    tmp += s[cur] * x
    x *= 10

    if s[cur] == 0:
        ans += 1
        tmp = 0
        x = 1
    else:
        tmp2 = tmp
        # print(tmp2)
        while tmp2 != 0:
            if tmp2 % 3 == 0:
                ans += 1
                tmp = 0
                x = 1
                break
            tmp2 //= 10

    cur -= 1

print(ans)
