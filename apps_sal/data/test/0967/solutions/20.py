num = int(input())
arr = list(map(int,input().split()))
i = num-1
while arr[i] > arr[i-1]:
    i -= 1
print(i)

