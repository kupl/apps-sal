s = input()
n = len(s) // 2
print('YNeos'[s[:n] != s[n + 1:]::2])
