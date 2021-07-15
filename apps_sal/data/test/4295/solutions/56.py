n,k = map(int,input().split())
check = []
check.append(n%k)
check.append(k-check[0])
print(min(check))
