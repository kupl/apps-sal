n = int(input())
nemog = set()
mog = set()
for i in range(26):
    mog.add(chr(97 + i))
    
cnt = 0
flag = False

for i in range(n):
    s = input()
    if s[0] == '.':
        for j in range(2, len(s)):
            mog.discard(s[j])
    if s[0] == '!':
        cnt += 1
        help = set()
        for j in range(2, len(s)):
            help.add(s[j])
        mog = mog & help
    if s[0] == '?':
        if i < n - 1:
            cnt += 1
            mog.discard(s[2])
        else:
            print(0)
            flag = True
    if len(mog) == 1:
        save = i
        break
if not flag:
    ans = 0
    for i in range (save + 1, n):
        s = input()
        if s[0] == '!' or (i < n - 1 and s[0] == '?'):
            ans += 1
    print(ans)
