cars= int(input())
ans= 0
ansline= []
for i in range(cars):
    inputline= [int(j) for j in input().split()]
    inputline= set(inputline)
    if 1 not in inputline and 3 not in inputline:
        ans+= 1
        ansline.append(i+1)
        

print(ans)
ansline.sort()
a= ""
if ans>0:
    for i in range(ans):
        a+= str(ansline[i])+ " "

print(a)
