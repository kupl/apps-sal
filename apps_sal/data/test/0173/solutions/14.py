(n, m) = map(int, input().split())
nstr = str(input())
mstr = str(input())
if nstr[0] == '>' and mstr[0] == 'v':
    print('NO')
    quit()
if nstr[0] == '<' and mstr[-1] == 'v':
    print('NO')
    quit()
if nstr[-1] == '>' and mstr[0] == '^':
    print('NO')
    quit()
if nstr[-1] == '<' and mstr[-1] == '^':
    print('NO')
    quit()
print('YES')
