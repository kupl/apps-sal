# cook your dish here
n = int(input())
arr = list(map(int, input().split()))
lst = arr[-1]
count = 0
for i in range(len(arr)-1,-1,-1):
    if(arr[i] == lst):
        count = count + 1
    else:
        break
print(len(arr)-count+1)



