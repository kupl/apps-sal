n = int(input())
s = list(input())
f = [0] + list(map(int, input().split()))
cok = 1
for i in range(n):
    q = int(s[i])
    if cok:
        if f[q] > q:
            cok = 0
            s[i] = str(f[q])
    else:
        if f[q] >= q:
            s[i] = str(f[q])
        else:
            print(''.join(s))
            return
print(''.join(s))
