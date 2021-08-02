xx, kk = input().split(' ')
x = int(xx)
k = int(kk)
used = []
for i in range(5005): used.append(0)
used[x] = 1
for i in range(k):
    p = [int(x) for x in input().split()]
    if p[0] == 1:
        used[p[1]] = used[p[2]] = 1
    if(p[0] == 2):
        used[p[1]] = 1
mn, mx = 0, 0
for i in range(x):
    if(i == 0): continue
    if(used[i] == 1):
        continue;
    j = i + 1
    while(used[j] == 0):
        used[j] = 1
        j = j + 1
    mx += j - i
    mn += (j - i + 1) // 2


print(mn, mx)
