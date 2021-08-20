(h, w) = map(int, input().split())
n = int(input())
al = list(map(int, input().split()))
res = []
for i in range(n):
    for j in range(al[i]):
        res.append(i + 1)
for k in range(h):
    temp = res[k * w:(k + 1) * w]
    if k % 2 == 1:
        temp = list(reversed(temp))
    else:
        pass
    print(str(temp).replace('[', '').replace(']', '').replace(',', ' '))
