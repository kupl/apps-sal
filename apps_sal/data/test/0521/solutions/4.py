n = int(input())
ch = input()
if 'CC' in ch or 'MM' in ch or 'YY' in ch:
    print('No')
elif '??' in ch:
    print('Yes')
elif ch[0] == '?':
    print('Yes')
elif ch[n - 1] == '?':
    print('Yes')
elif '?' not in ch:
    print('No')
else:
    x = False
    for i in range(1, len(ch) - 1):
        if ch[i] == '?':
            if ch[i - 1] == ch[i + 1]:
                x = True
                break
    if x:
        print('Yes')
    else:
        print('No')
