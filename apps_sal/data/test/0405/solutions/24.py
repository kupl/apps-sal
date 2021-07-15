n = int(input())
s = input()
if s[0] != '<' and s[-1] != '>':
    print(0)
elif s[0] != '<':
    if '<' in s:
        print(len(s) - s.rindex('<') - 1)
    else:
        print(len(s))
elif s[-1] != '>':
    if '>' in s:
        print(s.index('>'))
    else:
        print(len(s))
else:
    print(s.index('>') + len(s) - s.rindex('<') - 1)

