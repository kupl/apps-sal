N = int(input())
P = list(map(int, input().split()))
 
left_bigger  = [0] + [i for i in range(N+1)]
right_bigger = [i+1 for i in range(N+1)] + [N+1]
 
E = [(v, i+1) for i, v in enumerate(P)]
E.sort()

ans = 0
for v,i in E:
    l0=left_bigger[i]
    l1=left_bigger[l0]
    r0=right_bigger[i]
    r1=right_bigger[r0]
    
    ans += ((r1-r0)*(i-l0) + (r0-i)*(l0-l1))*v
    left_bigger[r0]=l0
    right_bigger[l0]=r0
print(ans)
