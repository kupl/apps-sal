for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    ans=-1
    for k in range(1,1025):
        st=set(s)
        for i in s:
            val=i^k 
            if val not in st:
                break
            st.remove(val)
        if not st:
            ans=k 
            break
    print(ans)
