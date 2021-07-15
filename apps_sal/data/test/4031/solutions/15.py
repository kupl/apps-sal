n = int(input())
arr = []
for _ in range(n): arr.append(input())
arr.sort(key=len)
for i in range(n):
    for j in range(i, -1, -1):
        if arr[j] not in arr[i]:
            print("NO")
            return
print("YES")
print(*arr, sep='\n')
