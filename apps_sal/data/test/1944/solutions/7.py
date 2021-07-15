lst = list(map(int, input().split()))
n=lst[0]
price=[]
quality=[]
data={};
for i in range(0,n):
    x = list(map(int, input().split()))
    data[x[0]]=x[1]
last=-1;
for key in sorted(data):
    if last>data[key]:
        print('Happy Alex')
        return
    last=data[key]
print('Poor Alex') 


