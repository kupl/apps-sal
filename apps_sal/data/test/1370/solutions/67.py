import sys
input = sys.stdin.readline

H,W,K=list(map(int,input().split()))
S = [input().rstrip() for _ in range(H)]

bit = 2**(H-1)
ans = (H-1)+(W-1)
for bi in range(bit):
    w = 0
    cnt = bin(bi).count('1')
    counter_1 = [0]*H
    
    while w <W:
        i=0
        for h in range(H):
            if S[h][w] == '1':
                counter_1[i]+=1
                if counter_1[i]>K:
                    cnt +=1
                    counter_1 = [0]*H
                    w -=1
                    break
            if bi >>h & 1:
                i+=1
        w+=1
        if cnt>=ans:
            break
    ans = min(ans,cnt)
print(ans)

