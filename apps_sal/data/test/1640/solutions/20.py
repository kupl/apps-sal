n = int(input())
v = [int(x) for x in input().split()]
mp = {}
s = sum(v)
ans = 0
cnt = n

for i in range(n):
    if v[i] in mp:
        mp[v[i]] += 1
    else:
        mp[v[i]] = 1

for i in range(n):
    c = v[i]
    s -= c
    cnt -= 1
    ans += (s - (cnt*c))
    ans -= mp.get(c+1, 0)
    ans += mp.get(c-1, 0)
    mp[c] -= 1
    
print(ans)
