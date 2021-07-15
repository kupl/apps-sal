n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = []
flag = True

for i in range(4):
    if len(res) == n:
        flag = True
        break
    flag = True
    res = [i]
    for k in range(0, n-1):
        if not flag:
            break
        for j in range(4):
            if (res[k] & j) == b[k] and (res[k] | j) == a[k]:
                res.append(j)
                break
        else:
            flag = False

if flag:
    print("YES")
    print(*res)
else:
    print("NO")

