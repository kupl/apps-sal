s = input()
n = len(s)
i = 0
a = [(0, 0) for x in range(0, 26)]
l = 0
b = 0
while i < n:
    if s[i] == '?':
        i += 1
        l += 1
    else:
        intc = ord(s[i]) - ord('A')
        if a[intc][0] == 0:
            # print("if",intc)
            a[intc] = (1, i)
            l += 1
            i += 1
        else:
            # print("else",intc)
            i = a[intc][1] + 1
            l = 0
            for k in range(0, 26):
                a[k] = (0, 0)
    if l == 26:
        b = 1
        i -= 26
        break
p = list(s)
if b == 0:
    print(-1)
else:
    for j in range(i, i + 26):
        if p[j] == '?':
            for k in range(0, 26):
                if a[k][0] == 0:
                    a[k] = (1, 0)
                    p[j] = chr(k + ord('A'))
                    break
    for j in range(0, n):
        if p[j] == '?':
            p[j] = 'A'
    w = "".join(p)
    print(w)
