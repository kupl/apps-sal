n = int(input())

arr = list(map(int, input().strip().split(' ')))
arr.sort()
if(n % 2 == 0):
    print(arr[n // 2 - 1])
else:
    print(arr[n // 2])
