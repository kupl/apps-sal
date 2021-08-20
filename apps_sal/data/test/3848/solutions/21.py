import sys
(n, p) = list(map(int, sys.stdin.readline().split()))
s = sys.stdin.readline()
sl = list(s)
sl.remove('\n')
flag = 0
for i in range(n - 1, -1, -1):
    c = ord(s[i]) - 96
    prev = -1
    nprev = -1
    if c < p:
        if i - 1 >= 0:
            prev = ord(s[i - 1]) - 96
            if i - 2 >= 0:
                nprev = ord(s[i - 2]) - 96
        flag = 0
        for j in range(c + 1, p + 1):
            if j != prev and j != nprev:
                sl[i] = chr(j + 96)
                flag = 1
                break
        if flag:
            break
sn = ''.join(sl).strip()
if s.strip() == sn:
    print('NO')
else:
    sn = sn[:i + 1]
    while i < n - 1:
        for j in range(26):
            if sn[-1] != chr(j + 97):
                if i > 0 and sn[-2] != chr(j + 97):
                    i += 1
                    sn += chr(j + 97)
                    break
                if i <= 0:
                    i += 1
                    sn += chr(j + 97)
                    break
    print(sn)
