n,k = list(map(int,input().split()))
ls = list(map(int,input().split()))
flag = True
if 0 not in ls:
    ls.append(0)
    ls.sort()
    flag = False
ind = ls.index(0)
if flag == True:
    if ind >= k-1:
        l = ind - k + 1
    else:
        l = 0
    if ind + k - 1 <= n - 1:
        r = ind + k - 1
    else:
        r = n - 1 
    mn = float("inf")
    while True:
        if l+k-1 > r:
            break
        a = abs(ls[l]) + ls[l+k-1] + min(abs(ls[l]),ls[l+k-1])
        if a < mn:
            mn = a
        l += 1
else:
    if ind >= k:
        l = ind - k
    else:
        l = 0
    if ind + k <= n:
        r = ind + k
    else:
        r = n
    mn = float("inf")
    while True:
        if l+k > r:
            break
        a = abs(ls[l]) + ls[l+k] + min(abs(ls[l]),ls[l+k])
        if a < mn:
            mn = a
        l += 1
print(mn)

