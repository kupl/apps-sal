n = int(input())
s = list(input())

s=s[::-1]
balance = 0
i = 0
while i < len(s):
    if s[i] == ')':
        balance+=1
    else:
        balance-=1
    if balance<0:
        s.insert(0, ')')
        balance+=1
        i+=1
    i+=1


balance = 0
i = 0
s=s[::-1]
while i < len(s):
    if s[i] == '(':
        balance+=1
    else:
        balance-=1
    if balance<0:
        s.insert(0, '(')
        balance+=1
        i+=1
    i+=1

print((''.join(s)))
    

