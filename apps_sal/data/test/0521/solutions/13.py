n = int(input())
s = input()
ans = 0
for i in range(1, n):
    if s[i - 1] == s[i] and s[i] != '?':
        ans = -1
        break
if ans == -1:
    print('No')
else:
    ans = 1
    for i in range(n):
        if s[i] == '?':
            if i - 1 >= 0 and i + 1 < n:
                if s[i - 1] == 'C' and s[i + 1] == 'Y' or (s[i - 1] == 'Y' and s[i + 1] == 'C') or (s[i - 1] == 'Y' and s[i + 1] == 'M') or (s[i - 1] == 'M' and s[i + 1] == 'Y') or (s[i - 1] == 'M' and s[i + 1] == 'C') or (s[i - 1] == 'C' and s[i + 1] == 'M'):
                    ans = ans * 1
                else:
                    ans = ans * 2
            else:
                ans = ans * 2
    if ans > 1:
        print('Yes')
    else:
        print('No')
