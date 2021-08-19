(n, m) = list(map(int, input().split()))
div1 = {}
div2 = {}
tot = n
ans = False
p = -1
q = 100000000000
for i in range(m):
    (a, b) = list(map(int, input().split()))
    if b > a:
        if a in div1:
            ans = True
        else:
            div1[b] = 1
            div2[a] = 1
            p = max(a, p)
            q = min(b, q)
    elif a in div2:
        ans = True
    else:
        div1[a] = 1
        div2[b] = 1
        p = max(b, p)
        q = min(a, q)
if ans:
    print(0)
else:
    tot = q - p - 1
    if tot < 0:
        print(0)
    elif tot == 0:
        print(1)
    elif len(div1) == 0 and len(div2) == 0:
        print(n - 1)
    else:
        print(tot + 1)
