n = int(input())
s = input()[:n]
for i in range(len(s)):
    if s[i] == '1':
        if i - 1 >= 0 and s[i - 1] != '0':
            print("No")
            return
        if i + 1 < len(s) and s[i + 1] != '0':
            print("No")
            return
    elif s[i] == '0':
        if (i - 1 < 0 or s[i - 1] == '0') and (i + 1 >= len(s) or s[i + 1] == '0'):
            print("No")
            return
print("Yes")

