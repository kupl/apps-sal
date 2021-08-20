s = input()
ans = 1
ans2 = 1
for i in range(len(s)):
    if s[len(s) - 1 - i] == '1':
        ans = (ans * 2 + ans2) % (10 ** 9 + 7)
    ans2 = ans2 * 3 % (10 ** 9 + 7)
print(ans)
