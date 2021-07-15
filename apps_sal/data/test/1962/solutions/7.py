n,k,l=[int(x) for x in input().split()]
ns=[int(x) for x in input().split()]
loc=-1
def judge(start,restb):
    length=loc-start+1
    if length-k>=(restb-1):
        return True
    return False

def func():
    nonlocal ns,loc
    if n==1:
        print(min(ns))
        return
    ns.sort()
    # print(ns)
    for i in range(n*k):
        if ns[i]>ns[0]+l:
            loc=i
            break
    if loc==-1:
        loc=n*k-1
    else:
        loc-=1
    if loc<n-1:
        print(0)
        return
    st=0
    rb=n
    ans=0
    while judge(st,rb):
        ans+=ns[st]
        st+=k
        rb-=1
        if rb==0:
            break
    if rb>0:
        ans+=ns[st]
        rb-=1
        for i in range(rb):
            ans+=ns[loc-i]
    print(ans)
    return
func()


