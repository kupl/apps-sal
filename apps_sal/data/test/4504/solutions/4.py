s = input()
for i in range(len(s)):
    s = s[:-1]
    if len(s) % 2 == 0:
        if s[:len(s) // 2] == s[len(s) // 2:]:
            print(len(s))
            break
