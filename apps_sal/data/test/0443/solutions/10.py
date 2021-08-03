n = int(input())
arr = list(map(int, input().strip().split(' ')))
m = min(arr)
ind = arr.index(m)
if(n == 1):
    print(-1)
elif(n == 2 and arr[0] == arr[1]):
    print(-1)
else:
    print(1)
    print(ind + 1)
