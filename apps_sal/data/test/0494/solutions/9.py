n, m = list(map(int, input().split()))
l = [int(k) for k in input().split()]
a = [0]*n
for i in range(m-1):
    curLeader = l[i] - 1
    nextLeader = l[i+1] - 1
    jump = abs((nextLeader - curLeader) % n)
    if jump==0: jump = n
    a[curLeader] = jump

def reqNum(leader, jump):
    ans = (leader+jump)%n
    if(ans==0): ans = n
    return ans
def simulate():
    for i in range(m-1):
        leader = l[i]
        jump = a[leader-1]
        if(not reqNum(leader, jump)==l[i+1]): return False
    return True

if simulate():
    s = set(range(1,n+1)).difference(set(a))
    for i in range(n):
        if a[i]==0:
            a[i] = s.pop()
    t = sorted(a)
    if(t==list(range(1,n+1))): print(*a)
    else: print(-1)
else: print(-1)

