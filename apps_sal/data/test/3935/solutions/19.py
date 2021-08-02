n = int(input())
l = list(map(int, input().split()))
arr = [0] * 65
ll = [0] * n
for i in range(n):
    cou = 0
    a = l[i]
    while a % 2 == 0:
        cou += 1
        a = a // 2
    arr[cou] += 1
    ll[i] = cou
# print(arr)
m = arr.index(max(arr))
res = []
rak = 0
for i in range(n):
    if(ll[i] == m):
        rak += 1
    else:
        res.append(l[i])
print(n - rak)
if(n - rak):
    print(*res)
