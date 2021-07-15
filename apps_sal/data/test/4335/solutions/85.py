n = int(input())
s = str(input())
if len(s) % 2 == 1:
    print('No')
else:
    t = len(s) // 2
    if s[t:] == s[:t]:
        print('Yes')
    else:
        print('No')
