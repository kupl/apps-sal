s = input()
ans = 1
n = len(s)
c = 1
for i in range(1, n):
    if(int(s[i]) + int(s[i - 1]) - 2 * int('0') == 9):
        c += 1
    else:
        if(c % 2 == 1 and c > 1):
            ans *= (c + 1) // 2
        c = 1
if(c % 2 == 1 and c > 1):
    ans *= (c + 1) // 2
print(ans)
