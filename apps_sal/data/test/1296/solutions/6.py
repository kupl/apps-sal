def func(c, k, s, n):
    nc = []
    for i in range(n):
        nc.append(c[i] + (i + 1) * (k + 1))
    nc.sort()
    val = sum(nc[:k + 1])
    if(val <= s):
        return val
    else:
        return -1


inp = input().split()
n = int(inp[0])
s = int(inp[1])
c = []
val = input().split()
i = 1
for v in val:
    c.append(int(v))
    i += 1
begin = 0
end = n - 1
flag = 0
while(begin <= end):
    mid = (begin + end) // 2
    if(func(c, mid, s, n) != -1):
        if(mid == n - 1):
            print(mid + 1, func(c, mid, s, n))
            flag = 1
            break
        if(func(c, mid + 1, s, n) == -1):
            print(mid + 1, func(c, mid, s, n))
            flag = 1
            break
        else:
            begin = mid + 1
    else:
        end = mid - 1
if(flag == 0):
    print("0 0")
