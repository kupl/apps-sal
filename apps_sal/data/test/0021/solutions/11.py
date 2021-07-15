n = int(input())
arr = [int(x) for x in input().split()]
ans = 0
for i in range(n):
    for j in range(i):
        arr[i], arr[j] = arr[j], arr[i]
        mini = min(arr)
        pos_mini = arr.index(mini)
        maxi = max(arr)
        pos_maxi = arr.index(maxi)
        
        ans = max(ans, abs(pos_maxi-pos_mini))
        arr[i], arr[j] = arr[j], arr[i]
print(ans)

