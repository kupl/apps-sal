n, a, b, c = map(int,input().split())
l = []
for i in range(n):
    l.append(int(input()))
ans = 10**9    
for ci in range(4**n):
    ci_ = [-1] * n
    cnt = [0] * 3
    ca, cb, cc = 0, 0, 0
    for cj in range(n):
        cx = ci & 3
        if cx == 0:
            ca += l[cj]
            cnt[0] += 1 
        elif cx == 1:
            cb += l[cj]
            cnt[1] += 1 
        elif cx == 2:
            cc += l[cj]
            cnt[2] += 1 
        ci >>= 2
    if ca == 0 or cb == 0 or cc == 0:
        continue
    
    cost = 0
    for i in range(3):
        if cnt[i] > 1:
            cost += 10 * (cnt[i]-1)
    cost += abs(a-ca) + abs(b-cb) + abs(c-cc)
    ans = min(ans, cost)
print(ans)
