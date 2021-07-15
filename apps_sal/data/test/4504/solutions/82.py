s = input()
while True:
    s = s[:-1]
    if s[0:len(s)//2] == s[len(s)//2:]:
        print(len(s))
        return
