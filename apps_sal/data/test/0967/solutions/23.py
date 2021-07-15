

t=int(input())
arr=list(map(int,input().split()))

i=t-1

while( i>0 and arr[i] > arr[i-1] ):
    i-=1
    
print(i)
