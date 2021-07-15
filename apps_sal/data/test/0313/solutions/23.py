n = int(input())
l = list(map(int, input().split()))
res = 0
for i in range(n):
    if l[i]: res += 1
    elif i > 0 and i < n - 1 and l[i - 1]and l[i + 1]: res += 1
    else: continue
print(res)    

