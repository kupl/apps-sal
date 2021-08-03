# cook your dish here
n = int(input())
arr1 = list(map(int, input().strip().split()))
arr2 = list(map(int, input().strip().split()))
key = arr2[0]
print(0, end=" ")
i = 1
while i < n:
    if arr1[i] >= key:
        key = arr2[i]
        print(i, end=" ")
    else:
        i += 1
