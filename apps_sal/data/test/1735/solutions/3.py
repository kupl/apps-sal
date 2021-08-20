n = input()
s = ''
m = 0
s += n[0]
for i in range(len(n) - 1):
    if len(s) > 0:
        if n[i + 1] == s[-1]:
            s = s[:len(s) - 1]
            m += 1
        else:
            s += n[i + 1]
    else:
        s += n[i + 1]
if m % 2 == 1:
    print('Yes')
else:
    print('No')
