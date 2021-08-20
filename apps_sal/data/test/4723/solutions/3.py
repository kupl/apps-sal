s = input()
t = input()
for i in range(len(s) - len(t) + 1)[::-1]:
    cnt = 0
    q = 0
    for j in range(len(t))[::-1]:
        if s[i + j] == '?':
            q += 1
        elif s[i + j] == t[j]:
            cnt += 1
    if cnt == len(t) - q:
        idx = i
        s = s[:idx] + t + s[idx + len(t):]
        for k in range(len(s)):
            if s[k] == '?':
                s = s[:k] + 'a' + s[k + 1:]
        print(s)
        break
else:
    print('UNRESTORABLE')
