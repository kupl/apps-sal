n=int(input())
arr=list(map(int,input().split()))
dict1={}
for i in arr:
    try:
        dict1[i]+=1
    except:
        KeyError
        dict1[i]=1
print(max(dict1.values()))
