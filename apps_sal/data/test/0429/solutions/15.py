def poss(ss):
    prr = [0 for i in range(26)]
    ques = 0
    for x in ss:
        if x == '?':
            ques += 1
        else:
            prr[ord(x) - 65] = 1
    return sum(prr) + ques == 26


def make(ss):
    prr = [0 for i in range(26)]
    for x in ss:
        if x != '?':
            prr[ord(x) - 65] = 1
    ans = ''
    for x in ss:
        if x == '?':
            for i in range(26):
                if prr[i] == 0:
                    ans += chr(i + 65)
                    prr[i] = 1
                    break
        else:
            prr[ord(x) - 65] = 1
            ans += x
    return ans


s = input()
l = len(s)
if l < 26:
    print(-1)
else:
    ans = ''
    i = 26
    suc = 0
    while i <= l:
        if poss(s[i - 26:i]):
            ans += make(s[i - 26:i])
            suc = 1
            break
        elif s[i - 26] == '?':
            ans += 'A'
        else:
            ans += s[i - 26]
        i += 1
    for j in range(i, l):
        if s[j] == '?':
            ans += 'A'
        else:
            ans += s[j]
    if suc:
        print(ans)
    else:
        print(-1)
