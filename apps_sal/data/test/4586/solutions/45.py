li = list(input())

if li[0] == li[1] and li[1] == li[2]:
    print('Yes')
elif li[1] == li[2] and li[2] == li[3]:
    print('Yes')
elif li[0] == li[1] and li[0] == li[2] and li[0] == li[3]:
    print('Yes')
else:
    print('No')
