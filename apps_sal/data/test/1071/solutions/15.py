s = input().split()
a1 = int(s[0])
a2 = int(s[1])
a3 = int(s[2])
s = input().split()
b1 = int(s[0])
b2 = int(s[1])
b3 = int(s[2])
n = int(input())
if (a1 + a2 + a3)%5 == 0:
    aa = (a1 + a2 + a3)//5
else:
    aa = (a1 + a2 + a3)//5 + 1

if (b1 + b2 + b3)%10 == 0:
    bb = (b1 + b2 + b3)//10
else:
    bb = (b1 + b2 + b3)//10 + 1

if aa + bb <= n:
    print('YES')
else:
    print('NO')


    
        

