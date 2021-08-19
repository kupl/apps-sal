s = input()
t = input()
if len(s) != len(t):
    print('No')
else:
    g = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(s)):
        if (s[i] in g) != (t[i] in g):
            print('No')
            break
    else:
        print('Yes')
