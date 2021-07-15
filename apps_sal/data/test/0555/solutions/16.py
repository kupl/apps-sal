s = input()
ans = ''
for i in range(len(s)):
    x = int(s[i])
    if i == 0 and x == 9:
        ans += str(x)
    elif 9 - x < x:
        ans += str(9 - x)
    else:
        ans += str(x)
print(int(ans), end='')
