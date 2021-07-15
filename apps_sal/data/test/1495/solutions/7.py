import itertools
n = int(input())
l = list(map(int, input().split()))

m = max(l) + 5
freq = [0 for _ in range(m)]
count= [0 for _ in range(m)]
vis  = [-1 for _ in range(m)]
for i  in range(n):
    q = [(l[i], 0)]
    pos = 0
    while len(q)>pos:
        top,c  = q[pos]
        pos+=1
        if(top>=m or vis[top]==i):
            continue
        vis[top]   = i
        freq[top] += 1
        count[top]+= c
        q.append((2*top, c+1))
        q.append((top//2,c+1))

ans = min(j for i,j in zip(freq, count) if i==n)
print(ans)
