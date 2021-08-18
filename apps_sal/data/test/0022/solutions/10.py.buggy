s = input()
good = ['A', 'H', 'I', 'M', 'O', 'o', 'T', 'U', 'V', 'v', 'W', 'w', 'X', 'x', 'Y']
for i in range(len(s) // 2):
    if (s[i] == s[len(s) - i - 1] and s[i] in good) or (s[i] == 'b' and s[len(s) - i - 1] == 'd') or (s[i] == 'p' and s[len(s) - i - 1] == 'q') or (s[i] == 'd' and s[len(s) - i - 1] == 'b') or (s[i] == 'q' and s[len(s) - i - 1] == 'p'):
        pass
    else:
        print("NIE")
        return
if len(s) % 2 == 1:
    if s[len(s) // 2] in good:
        print("TAK")
    else:
        print("NIE")
else:
    print("TAK")
