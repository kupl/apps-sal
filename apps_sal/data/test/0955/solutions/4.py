from sys import stdin, stdout


n = int(stdin.readline())
mp = {}

for i in range(n):
    c, s = stdin.readline().strip().split()
    s = ''.join(sorted(list(s)))
    
    
    c = int(c)
    if not s in mp:
        mp[s] = c
    else:
        mp[s] = min(mp[s], c)

ans = float('inf')
for v in mp:
    for c in mp:
        for g in mp:
            if len({v, c, g}) != 3:
                continue
            
            if len(set(list(v)) | set(list(c)) | set(list(g))) != 3:
                continue
            
            ans = min(ans, mp[v] + mp[c] + mp[g])



for c in mp:
    for g in mp:
        if len({c, g}) != 2:
            continue
        
        if len(set(list(c)) | set(list(g))) != 3:
            continue
        
        ans = min(ans, mp[c] + mp[g])


for v in mp:
    
    if len(set(list(v))) != 3:
        continue
    
    ans = min(ans, mp[v])            
            

if ans == float('inf'):
    stdout.write('-1\n')
else:
    stdout.write(str(ans))
