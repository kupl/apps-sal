n1 = int(input())
a1 = list(map(int, input().split()))
n2 = int(input())
a2 = list(map(int, input().split()))
if n1 < n2:
    a1, a2 = a2, a1
if sum(a1) != sum(a2):
    print(-1)
else:
    c = 1
    f = 0
    s = 0
    c1 = a1[f]
    c2 = a2[s]    
    while s + 1 < len(a2) and f + 1 < len(a1):
        if c1 == c2:
            f += 1
            s += 1              
            c += 1
            c1 = a1[f]
            c2 = a2[s]             
        elif c1 > c2:
            s += 1
            c2 += a2[s]            
        else:
            f += 1
            c1 += a1[f]
    print(c)
