n, k = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]
offs = ord("a")
 
ans = [chr(offs+k-1)] * n
# ans = ""
pmore = set()
qmore = set()
 
let = 0
# cnt = 0
for i in range(n):
    # cnt += 1
    pi = p[i]
    qi = q[i]
    if qi in pmore:
        pmore.remove(qi)
    else:
        qmore.add(qi)
    if pi in qmore:
        qmore.remove(pi)
    else:
        pmore.add(pi)
 
    ans[pi - 1] = chr(let+offs)
    if len(pmore) + len(qmore) == 0:
        
        let += 1
        if let == k:
            break
 
 
 
if let == k:
    # if len(ans) < n:
    #     ans += chr(offs+k-1) * (n- len(ans))
    print("YES")
    print("".join(ans))
else:
    print("NO")
