n = int(input())
s = input()
while True:
    c = 0
    for i in range(len(s)):
        if s[i] == '(':
            c += 1
        else:
            c -= 1
        if c < 0:
            s = '(' + s
            break
    if c > 0:
        s = s + ')'
    if c == 0:
        print(s)
        break
