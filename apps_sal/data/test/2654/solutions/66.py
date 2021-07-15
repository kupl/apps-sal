from numpy import*
(n,),*d=[int_(i.split())for i in open(0)]
a,b=median(d,0)
print(int((b-a)*(2-n%2))+1)
