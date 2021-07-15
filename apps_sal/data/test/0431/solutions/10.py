n,m = map(int, input().split())
h = []
l = []
r = []
last = -1
for i in range(n):
    s = input()
    h.append(s)
i=0
for s in reversed(h):
    lp, rp = m+1, 0
    for j in range(len(s)):
        let = s[j]
        if let == '1' and lp == m+1:
            lp = j
        if let == '1':
            rp = j
    l.append(lp)
    r.append(rp)
    if r[i] != 0 or l[i] != m+1:
        last = i
    i+=1
        
        
dp = [[2*r[0], m + 1]] 
for i in range(1,last):
    prev = dp[-1]
    ml = min(prev[0] + 2*r[i], prev[1] + m + 1) + 1
    rl = min(prev[1] + 2*(m+1 - l[i]), prev[0] + m+1) + 1
    dp.append([ml, rl])
    
if last == 0:
    ans = r[0]
elif last == -1:
    ans = 0
else:
    ans = min(dp[-1][0] + r[last] + 1, dp[-1][1] + (m +1 - l[last]) + 1)

print(ans)
