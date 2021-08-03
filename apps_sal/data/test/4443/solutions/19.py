c = input()
s = list('abcdefghijklmnopqrstuvwxyz')

for i in range(25):
    if c == s[i]:
        print(s[i + 1])
        return
