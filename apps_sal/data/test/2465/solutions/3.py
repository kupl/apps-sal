T=int(input())
Q=[int(input()) for i in range(T)]

LIST=[None]*181

for i in range(3,361):
    for k in range(1,i-1):
        if 180*k%i==0 and LIST[180*k//i]==None:
            LIST[180*k//i]=i

LIST[180]=-1      
for q in Q:
    print(LIST[q])

