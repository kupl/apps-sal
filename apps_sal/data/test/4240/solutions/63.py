s=input()
t=input()
Flag=False
for _ in range(len(s)):
    s=s[-1]+s[:-1]
    if s==t:
        Flag=True
if Flag:
    print('Yes')
else:
    print('No')
