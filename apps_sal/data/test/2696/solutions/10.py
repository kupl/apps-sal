n = int(input())
arr = list(map(int, input().split()))
tar = arr[n - 1]
j = n - 2
flag = 0
while(j > 0):
    if(arr[j] == tar):
        tar = arr[j]
        j = j - 1
        continue
    else:
        flag = j + 1
        break
print(str(flag + 1))
