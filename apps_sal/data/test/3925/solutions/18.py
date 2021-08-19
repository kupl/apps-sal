import sys
f = sys.stdin
s = f.readline().rstrip('\r\n')
arr = []
cnt = 1
ma = 0
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        cnt += 1
    else:
        ma = max(ma, cnt)
        cnt = 1
ma = max(ma, cnt)
if ma == len(s):
    print(str(ma) + '\n')
else:
    cnt1 = 1
    cnt2 = 1
    if s[0] != s[-1]:
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                cnt1 += 1
            else:
                break
        for i in range(len(s) - 1, 0, -1):
            if s[i] != s[i - 1]:
                cnt2 += 1
            else:
                break
        ma = max(ma, cnt1 + cnt2)
    sys.stdout.write(str(ma) + '\n')
