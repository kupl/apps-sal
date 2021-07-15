n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
first = min(a[0],b[0])
more = min(a[1],b[0]-first)
count = first + more
for i in range(1,n):
    first = min(a[i]-more,b[i])
    more = min(a[i+1],b[i]-first)
    count +=  first + more
print(count)
