n,k = map(int,input().split())
s = list(input())

if s[k - 1] == 'A':
    s[k - 1] = 'a'
if s[k - 1] == 'B':
    s[k - 1] = 'b'
if s[k - 1] == 'C':
    s[k - 1] = 'c'
strA = ''.join(s)
print(strA)
