h,m,s,t1,t2=list(map(int,input().split()))
m+=s/60
h+=m/60
m/=5
s/=5
h=h%12
m=m%12
s=s%12
T1=min(t1,t2)
T2=max(t1,t2)
if(T1<h<T2 and T1<m<T2 and T1<s<T2):
    print("YES")
elif(not(T1<h<T2 or T1<m<T2 or T1<s<T2)):
    print("YES")
else:
    print("NO")



