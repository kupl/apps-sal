N = int(input())
 
arr = input()
arr = [int(x) for x in arr.split(' ')]

arr.sort()

if arr[-1]>=arr[-2]+arr[-3]:
    print('NO')
else:
    print('YES')
    tmp = arr[-2]
    arr[-2] = arr[-1]
    arr[-1] = tmp
    for i in range(N):
        print(arr[i],end=' ')
 

