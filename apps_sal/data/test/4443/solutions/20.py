c = input()
s = list('abcdefghijklmnopqrstuvwxyz')

for i in range(len(s)):
    if c == s[i]:
        print(s[i + 1])
        return
