n, k=map (int, input (). split ()) 
a=list (map (int, input (). split ())) 
a=sorted (a) 
ans=0
for i in range (min(k, n) ):
    ans+=a[i] 
print (ans) 
