s = input()
n = len(s)
check = True
for i in range(n):
    if s[i] != s[n - i - 1]:
        check = False
for i in range((n - 1) // 2):
    if s[i] != s[(n - 1) // 2 - i - 1]:
        check = False
    if s[i + (n + 1) // 2] != s[n - i - 1]:
        check = False
print("Yes" if check else "No")
