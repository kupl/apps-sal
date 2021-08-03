a, b = map(int, input().split())
s = list(input())
if s[a] == '-':
    c = 0
    for i in range(0, a + b + 1):
        if s[i].isdecimal() == True:
            c = c + 1
    if c == a + b:
        print('Yes')
    else:
        print('No')
else:
    print('No')
