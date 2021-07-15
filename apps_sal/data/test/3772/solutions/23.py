s=input()
[a,b]=(s.split())
a=int(a)
b=int(b)
if b>a: a,b=b,a
ans=0
while b!=0:
    c=a%b
    ans+=(a//b)
    a=b
    b=c
print(ans,end="\n")

 		 	 		  	    		  			 	 			
