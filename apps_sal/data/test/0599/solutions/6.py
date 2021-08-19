def f(s):
    at = -1
    for (i, v) in enumerate(s):
        if v == '@':
            at = i
            continue
        if v != s[-i - 1] and s[-i - 1] != '@':
            return False
    s[at] = s[-at - 1]
    return ''.join(s)


s = list(input())
for i in range(len(s) + 1):
    s.insert(i, '@')
    a = f(s)
    if a:
        print(a)
        break
    del s[i]
else:
    print('NA')
