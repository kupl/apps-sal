import sys
t = int(input())
req = 'abacaba'
for _ in range(t):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().rstrip()
    cnt = 0
    for i in range(n - 6):
        if s[i:i + 7] == req:
            cnt += 1
    if cnt == 1:
        print('Yes')
        print(s.replace('?', 'z'))
        continue
    if cnt > 1:
        print('No')
        continue
    for i in range(n - 6):
        if all((c1 == c2 or c1 == '?' for (c1, c2) in zip(s[i:i + 7], req))):
            if s[i + 7:i + 11] == 'caba' or (i >= 4 and s[i - 4:i] == 'abac'):
                continue
            s = s[:i] + req + s[i + 7:]
            print('Yes')
            print(s.replace('?', 'z'))
            break
    else:
        print('No')
