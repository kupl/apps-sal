s = input()
for i in range(len(s) - 1, 0, -1):
    L = len(s[:i])
    if L % 2 == 0 and s[:L // 2] == s[L // 2:L]:
        print(i)
        return
