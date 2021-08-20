s = input()
if len(s) % 2 == 0:
    number = s[len(s) // 2]
    other = s[len(s) // 2 - 1]
    p = len(s) // 2
    cnt = 0
    if number == other:
        cnt += 1
        for i in range(1, p):
            if s[p + i] == s[p - 1 - i] == number:
                cnt += 1
            else:
                break
    print(p + cnt)
else:
    number = s[len(s) // 2]
    cnt = 0
    p = len(s) // 2
    for i in range(1, len(s) // 2 + 1):
        if s[p - i] == s[p + i] == number:
            cnt += 1
        else:
            break
    print(p + 1 + cnt)
