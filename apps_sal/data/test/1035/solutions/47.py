def factrization(n):
    arr = []
    temp = n
    for i in range(2, int(n ** 0.5 // 1) + 2):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append(i)
    if temp != 1:
        arr.append(temp)
    if arr == []:
        arr.append(n)
    return arr


(a, b) = map(int, input().split())
ans = 0
la = factrization(a)
lb = factrization(b)
if 1 not in la:
    la.append(1)
if 1 not in lb:
    lb.append(1)
for i in la:
    if i in lb:
        ans += 1
print(ans)
