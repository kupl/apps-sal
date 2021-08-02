W = input()
ans = 'Yes'

if len(W) % 2 == 0:
    W_ele = set([w for w in W])
    for w in W_ele:
        if W.count(w) % 2 == 1:
            ans = 'No'
else:
    ans = 'No'
print(ans)
