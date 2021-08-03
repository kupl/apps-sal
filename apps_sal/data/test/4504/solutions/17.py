s = input()
while len(s) != 0:
    s = s[:-2]
    le = round(len(s) / 2)
    if s[:le] == s[le:len(s)]:
        print(len(s))
        break
