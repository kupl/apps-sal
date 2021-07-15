s=str(input())
n=int(input())
found = False
for i in range(n):
    a = str(input())
    if len(a) == len(s):
        similar = True
        for j in range(len(a)):
            ac = a[j].capitalize()
            sc = s[j].capitalize()
            if ac != sc:
                if ac in ('0', 'O') and sc in ('0', 'O') or ac in ('1', 'I', 'L') and sc in ('1', 'I', 'L'):
                    similar = True
                else:
                    similar = False
                    break
        if similar:
            found = True
if found:
    print('No')
else:
    print('Yes')

