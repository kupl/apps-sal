h,w,k = list(map(int,input().split()));arr = [[int(i) for i in input()] for _ in range(h)]

from itertools import product
ans = 2000

for i in product([True,False],repeat=(h-1)):
    cut = sum(i)
    splits = [0] * (cut+1)
    splits[0] = arr[0][:]
    tmp = 0
    div = cut
    for j in range(1,h):
        if i[j-1]:
            tmp += 1
            splits[tmp] = arr[j][:]
        else:
            splits[tmp] = [splits[tmp][idx]+arr[j][idx] for idx in range(w)]
    
    check = 0
    for j in splits:
        check = max(check,max(j))
    if check > k:
        break
    count = [splits[j][0] for j in range(cut+1)]
    
    for j in range(1,w):
        addarr = [count[idx]+splits[idx][j] for idx in range(cut+1)]
        if max(addarr) > k:
            div += 1
            count = [splits[idx][j] for idx in range(cut+1)]
        else:
            count = addarr[:]
    ans = min(ans,div)
        
print(ans)
