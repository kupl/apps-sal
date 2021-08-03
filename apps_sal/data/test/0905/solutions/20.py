'''n, s=map(int, input().split())
d=[]
c=-1
while(n>0):
    n-=1
    [xi, yi]=map(int, input().split())
    d.append([xi, 100-yi])
for i in d:
    if(i[0]+((100-i[1])/100)<=s):
        if(i[1]>c and i[1]!=100):
            c=i[1]
print(c)'''
n, s = list(map(int, input().split()))
c = -1
for i in range(n):
    xi, yi = list(map(int, input().split()))
    if(yi == 0 and xi <= s):
        c = max(0, c)
    elif(xi < s):
        c = max(100 - yi, c)
print(c)
