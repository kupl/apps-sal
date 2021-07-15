n = int(input())
arr = sorted([int(i) for i in input().strip().split(' ')])
print(arr[len(arr)//2])
