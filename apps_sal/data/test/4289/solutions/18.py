n = int(input())
t,a = map(int,input().split())
li = list(map(int,input().split()))
lis = []
for i in li:
    lis.append(abs((t-i*0.006)-a))
print(lis.index(min(lis))+1)
