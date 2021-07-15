n = int(input())
arr = list(map(int, input().split()))
s = sum(arr)*2
z = round(s / (2*n))
for k in range(n):
    arr[k] = (arr[k]-z) ** 2
print((sum(arr)))

