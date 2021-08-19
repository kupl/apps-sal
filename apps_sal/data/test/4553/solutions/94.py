# 33
A, B = map(int, input().split(' '))
S = str(input())

ans = 'Yes'
if S[A] != '-':
    ans = 'No'
else:
    S = S.replace('-', '', 1)
    if S.isdecimal() == False:
        ans = 'No'

print(ans)
