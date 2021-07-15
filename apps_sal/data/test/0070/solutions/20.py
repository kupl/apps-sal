n, k = list(map(str, input().split()))
k = int(k)

n = n[::-1]

cc = 0
cz = 0
c = len(n)
for i in range(c):
    if int(n[i]) == 0:
        cz += 1
    else:
        if cz >= k:
            break
        else:
            cc += 1
if cz < k:
    print(c - 1)
else:
    print(min(c - 1, cc))

