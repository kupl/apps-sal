n, k = list(map(int, input().split()))
X = [int(a) for a in input().split()]
s = input()

i = 1
p = s[0]
l = [X[0]]
c = 1
ans = 0
while i <= n:
    if i < n and p == s[i]:
        l.append(X[i])
        c += 1
    else:
        if len(l) <= k:
            ans += sum(l)
        else:
            l = sorted(l)
            ans += sum(l[-k:])

        if i == n:
            break
            
        l = [X[i]]
        p = s[i]
        c = 1
    
    
    i += 1
print(ans)

