s = input()
c = s[0]
cnt = 1
ma = 1
for i in range(1, len(s)):
    if s[i] != c:
        cnt += 1
        c = s[i]
    else:
        ma = max(ma, cnt)
        cnt = 1
        c = s[i]
ma = max(ma, cnt)
if s[0] == s[-1] or len(s) <= 2:
    print(ma)
else:
    cnt = 1
    c = s[0]
    for i in range(1, len(s)):
        if s[i] != c:
            cnt += 1
            c = s[i]
        else:
            break
    cnt += 1
    c = s[-1]
    for i in range(2, len(s) + 1):
        if s[-i] != c:
            cnt += 1
            c = s[-i]
        else:
            break
    cnt = min(len(s), cnt)
    print(max(cnt, ma))
