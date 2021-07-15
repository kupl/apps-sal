raselBhai = lambda:list(map(int,input().split()))

n = int(input())
lst = raselBhai()
m = 10**5+5
dst = [-1] * m
pst = [-1] * m
for i in range(n):
    if pst[lst[i]] == -1:
        dst[lst[i]] = 0
    else:
        if i - pst[lst[i]] != dst[lst[i]]:
            if dst[lst[i]] == 0:
                dst[lst[i]] = i - pst[lst[i]]
            else:
                dst[lst[i]] = -1
    pst[lst[i]] = i
cnt = 0
for i in range(m):
    if dst[i] != -1:
        cnt += 1
print(cnt)
'''for i in range(m):
    if dst[i] != -1:
        print('\n'.join("{0} {1}".format(dst[i])))'''
print('\n'.join("{0} {1}".format(i, dst[i]) for i in range(m) if dst[i] != -1))

