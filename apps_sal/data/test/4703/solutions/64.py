s = input()

ans = 0

for i in range(1 << (len(s) - 1)):
    t = list(s)
    for b in range(len(s) - 1):
        if((i >> b) & 1):
            t[b] = t[b] + '+'
    ans += eval(''.join(t))
print(ans)
