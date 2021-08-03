n, m = list(map(int, input().split()))
pieces = []
s = None
f = None
flag = True
opn = False
for k in range(n):
    line = input()
    i = 0
    j = len(line) - 1

    while i < m:
        if line[i] == 'X':
            if not(s is None or i == s):
                flag = False
                break
            else:
                s = i
                break
        i += 1
    i = 0
    while i < m:
        if line[i] == 'X':
            if i != 0 and line[i - 1] == '.' and opn:
                flag = False
                break
        if line[i] == '.' and i != 0 and line[i - 1] == 'X':
            opn = True
        i += 1
    opn = False
    while j > -1:
        if line[j] == 'X':
            if not(f is None or j == f):
                flag = False
                break
            else:
                f = j
                break
        j -= 1
if flag:
    print("YES")
else:
    print("NO")
