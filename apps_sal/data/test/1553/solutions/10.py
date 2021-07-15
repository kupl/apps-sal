n, k = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

heights = []
ok= 0
for jj in range(n+1):
    heights = sorted(A[:jj], reverse=True)
    totalheight = 0
    for i in range(len(heights)):
        if i&1:
            continue
        else:
            totalheight+=heights[i]
    
    #print('at jj',jj, totalheight)
    if totalheight <= k:
        ok = jj
    else:
        break
print(ok)

