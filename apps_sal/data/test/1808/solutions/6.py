N, K, X = list(map(int, input().split()))

arr = list(map(int, input().split()))

res = sum(arr[0:-K])
res += X * K
print(res)
