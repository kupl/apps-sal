s = input()
while True:
    l = len(s)
    s = s[:l - 1]
    if len(s) % 2 != 0:
        pass
    elif s[:len(s) // 2] == s[len(s) // 2:]:
        print(len(s))
        break
