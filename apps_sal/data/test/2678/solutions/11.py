import sys 
input = sys.stdin.readline 

N=int(input())
arr=[]
for i in range(N):
    k=list(map(int,input().split()))
    arr.append(k)
arr.sort()
end=arr[0][1]
count=1 
for j in range(1,len(arr)):
    if(arr[j][0]<=end):
        if(arr[j][1]<=end):
            end=arr[j][1]
        else:
            pass 
    else:
        count+=1 
        end = arr[j][1]
print(count)
