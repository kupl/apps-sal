n = int(input())
arr = list(map(int, input().split()))
mishka = arr[0]
arr[0] = -1

ans = 0

while(mishka < max(arr) and mishka != max(arr)):
    mishka += 1
    arr[arr.index(max(arr))] = max(arr) - 1
    ans += 1

if(mishka == max(arr)):
    ans += 1

print(ans)
