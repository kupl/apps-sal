from copy import deepcopy as copy


H, W, K = list(map(int, input().split()))
c = [list(input()) for i in range(H)]

ans = 0

for i in range(2**H):
    cc = copy(c)
    n = i
   
    idx = -1
    while n > 0:
        x = n % 2
        n //= 2
        idx += 1
        if x == 0: continue
        
        for j in range(W):
            cc[idx][j] = '.'
            
    for j in range(2**W):
        ccc = copy(cc)
        n = j
        idx = -1
        
        while n > 0:
            x = n % 2
            n //= 2
            idx += 1
            if x == 0: continue
        
            for k in range(H):
                ccc[k][idx] = '.'
                
        cnt = sum([_.count('#') for _ in ccc])
        
        if cnt == K: ans += 1
print(ans)
