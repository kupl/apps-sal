p, n = list(map(int, input().split()))
arr = [-1 for i in range(1000)]
for i in range(n):
    x = int(input())
    if arr[x % p] != -1:
        print(i + 1)
        return
    else:
        arr[x % p] = x
print(-1)
