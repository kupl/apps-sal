n = int(input())
h = list(map(int, input().split()))

ans = 0
def solve(li_h):
    l = 0
    for i in li_h:
        if(i==0):
            l += 1
        else:
            break
    r = l + 1
    for i in li_h[l+1:]:
        if(i==0):
            break
        r += 1
    
    for i in range(l, r):
        li_h[i] -= 1
    
    return li_h

while(sum(h)!=0):
    h = solve(h)
    ans += 1

print(ans)
