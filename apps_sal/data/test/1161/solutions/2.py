s = input()

open = '[<({'
close = ']>)}'

clopen = { ']': '[', '}': '{', '>': '<', ')': '(' }
popen = []
c = 0
for i in range(len(s)):
    if s[i] in open:
        popen.append(s[i])
    else:
        if len(popen) == 0:
            print('Impossible')
            return
        p = popen.pop()
        if clopen[s[i]] != p:
            c += 1

print(c if len(popen) == 0 else 'Impossible')

