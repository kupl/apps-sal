s = input()

n = int(input())
for i in range(n):
    t = input()
    if len(s) != len(t):
        continue
    for j in range(len(t)):
        if t[j].lower() == s[j].lower():
            continue
        if t[j] in '0Oo' and s[j] in '0Oo':
            continue
        if s[j] in '1lILi' and t[j] in '1lILi':
            continue
        # print(s[j], t[j], s, t, i)
        break
    else:
        print('No')
        return
print('Yes')
