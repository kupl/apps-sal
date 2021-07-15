n,m = list(map(int, input().split()))

bt = sum([i for i in range(1,m-n+1)])
print(bt-m)
