def rev(arr):
    cop = arr.copy()
    cop.reverse()
    return cop
try:
    n = int(input())
    s=[]
    ans =[]
    data = list(input())
    for i in range(n):
        s.append(data[i])
        for j in range(i+1,n):
            s.append(data[j])
            if(s == rev(s)):
                ans.append(''.join(rev(s)))
        s.clear()
        
    r = max(ans,key=len)
    print(len(r))
    print(r)
except:
    pass
