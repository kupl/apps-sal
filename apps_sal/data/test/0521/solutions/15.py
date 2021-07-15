n = int(input())
s = input().rstrip()
notpaint = []
flg = True
for i in range(n):
    if i < n-1 and s[i] != '?':
        if s[i] == s[i+1]:
            flg = False
            break
    if s[i] == '?':
        notpaint.append(i)
if flg:
    work = 1
    for q in notpaint:
        if 0 == q or n-1 == q:
            work *= 2
        else:
            if s[q-1] == s[q+1] or s[q-1] == '?' or s[q+1] == '?':
                work *= 2
    if work > 1:
        print('Yes')
    else:
        print('No')
else:
    print('No')
