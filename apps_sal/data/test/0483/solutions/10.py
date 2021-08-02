n = int(input())
s = input()
ans = 1234567890
i = 0
last_r = -1
for x in input().split():
    now = int(x)
    if s[i] == 'R':

        last_r = now
    else:
        if last_r != -1:
            ans = min(ans, (now - last_r) // 2)

    i += 1
if ans == 1234567890:
    print('-1')
else:
    print(ans)
