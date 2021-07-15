n = int(input())
k = input().split()
s = 0
x = '1'
for i in range(n):
    if k[i] == '0':
        print('0')

        break
    elif  k[i].count('0') + k[i].count('1') != len(k[i]) or k[i].count('1') >1:
        x = k[i]
        
    else:
        s+=k[i].count('0')
        
        
else:
    print(x+'0'*s)
    

