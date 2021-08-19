def visit(arr, i, visited):
    ans = []
    temp = arr[i]
    ans.append(i)
    visited[i] = 1
    if temp == arr[temp]:
        ans.append(temp)
        return ans
    while temp != arr[temp]:
        ans.append(temp)
        if visited[i] == 1 and temp == i:
            break
        visited[temp] = 1
        temp = arr[temp]
    return ans


n = int(input())
arr = [0]
arr1 = list(map(int, input().split()))
for i in arr1:
    arr.append(i)
visited = [0] * (n + 1)
x = []
for i in range(1, n + 1):
    if visited[i] == 0:
        x.append(visit(arr, i, visited))
print(len(x))
for i in x:
    print(*i)
