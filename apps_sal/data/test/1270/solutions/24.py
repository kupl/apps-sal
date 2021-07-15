q=int(input())
if q%2==1:
    s=(q-2) // 2+1
else:
    s=q // 2
print(s)
print('2 '*s if q%2==0 else '2 '*(s-1)+'3')
