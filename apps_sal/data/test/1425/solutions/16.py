def arun(arr):
    return sorted(arr)


n = int(input())
arr = list(map(int, input().split()))
arr = arun(arr)
arr = arr[:n - 2] + [arr[-1]] + arr[n - 2:n - 1]
ans = ["NO", "YES"]
ind = 1
for i in range(n):
    if(arr[i] >= arr[(i - 1)] + arr[(i + 1) % n]):
        ind = 0
        print(ans[0])
if(ind):
    print(ans[1])
    for i in range(n):
        print(arr[i], end=" ")
    print()
