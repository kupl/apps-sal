N = int(input())
K = int(input())

res = 1
for i in range(N):
    if(K >= res):
        res *= 2
    else:
        res += K
print(res)
