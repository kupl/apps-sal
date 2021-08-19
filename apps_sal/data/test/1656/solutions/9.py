s = input()
n = len(s)
ldp = [0 for i in range(n)]
rdp = [0 for i in range(n)]
consec = 0
for i in range(n):
    if s[i] == 'v':
        consec += 1
    else:
        consec = 0
    if consec > 1:
        ldp[i] = ldp[i - 1] + 1
    else:
        ldp[i] = ldp[i - 1]
consec = s[-1] == 'v'
for i in range(n - 2, -1, -1):
    if s[i] == 'v':
        consec += 1
    else:
        consec = 0
    if consec > 1:
        rdp[i] = rdp[i + 1] + 1
    else:
        rdp[i] = rdp[i + 1]
ans = 0
for i in range(n):
    if s[i] == 'o':
        ans += ldp[i] * rdp[i]
print(ans)
