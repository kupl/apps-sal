import sys
input = sys.stdin.readline
y = int(input())
for i in range(y):
    n = int(input())
    arr = list(map(int, input().split()))
    a = 0
    visited = [0] * n

    for j in range(n):
        for k in range(n - 1, 0, -1):
            if(visited[k - 1] == 0 and arr[k - 1] > arr[k]):
                visited[k - 1] = 1
                temp = arr[k - 1]
                arr[k - 1] = arr[k]
                arr[k] = temp

    s = ""
    for j in arr:
        s = s + str(j) + " "
    s = s[:-1]
    print(s)
