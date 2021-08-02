n, m, k = map(int, input().split())
arr = []
for _ in range(m + 1):
    arr.append(int(input()))
lol = arr[m]
res = 0

for i in range(m):
    tmp = 0
    for j in range(n + 1):
        if((lol ^ arr[i]) & (2**j) != 0):
            tmp += 1
    if(tmp <= k):
        res += 1
print(res)
