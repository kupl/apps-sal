a=int(input())
s=''
for i in range(0,a):
    s=s+input()
x=1
x=x+s.count('11')
x=x+s.count('00')
print(x)
