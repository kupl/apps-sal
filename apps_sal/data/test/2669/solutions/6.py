n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
x = brr[0]
print(0, end=" ")
for i in range(n):
    if arr[i] >= x:
        print(i, end=" ")
        x = brr[i]
