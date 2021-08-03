s = input()
n = len(s)
ans = 1
cnt = 1
for i in range(n - 1):
    if(int(s[i]) + int(s[i + 1]) == 9):
        cnt += 1
    else:

        if(cnt % 2 == 1):
            ans = ans * (cnt // 2 + 1)
        cnt = 1
if(cnt % 2 == 1):
    ans = ans * (cnt // 2 + 1)
print(ans)
