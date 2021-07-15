numline=input().split(" ")
a=int(numline[0])
b=int(numline[1])

numline=input().split(" ")
numlis=[]
for i in range(a):
    numlis.append(int(numline[i]))

numlis.sort()

result=0
for i in range(b):
    result+=numlis[i]

print(result)
