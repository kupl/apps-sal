n = int(input())
res = 1
res *= n*n
res *= (n-1)*(n-1)
res *= (n-2)*(n-2)
res *= (n-3)*(n-3)
res *= (n-4)*(n-4)
res = res // 5 // 4 // 3 // 2 // 1
print(res)
