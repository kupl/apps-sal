n = input()
s = input()
bad = 'aeiouy'
while True:
    ok = True
    for i in range(1, len(s)):
        if s[i] in bad and s[i - 1] in bad:
            s = s[:i] + s[i + 1:]
            ok = False
            break
    if ok:
        print(s)
        break
