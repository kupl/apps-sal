S = input()
ans = 'AC'

if S[0] != 'A':
    ans = 'WA'

if S[2:-1:1].count('C') != 1:
    ans = 'WA'

S = S.replace('A', 'a').replace('C', 'c')

if S.islower() == False:
    ans = 'WA'

print(ans)
