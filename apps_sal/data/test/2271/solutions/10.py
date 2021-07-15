#from random import randrange
#import time
 
#class Profiler(object):
    #def __enter__(self):
    #    self._startTime = time.time()
         
    #def __exit__(self, type, value, traceback):
     #   print ("Elapsed time: {:.10f} sec".format(time.time() -self._startTime))

#masa = [randrange(1, 10000) for i in range(10000)]
#masb = [randrange(1, 10000) for i in range(10000)]

  
def UpperBound(A, key): 
    left = -1 
    right = len(A) 
    while right > left + 1: 
        middle = (left + right) // 2 
        if A[middle] > key: 
            right = middle 
        else: 
            left = middle
 
    return right
n=int(input())
masa=[]
masb=[]
mas=[]
for i in range(n-1):
   mas.append(input().split())
s=0 
#with Profiler() as p:
   # mas= [(100, 67), (1, 2), (4, 5)]
for i in range(n-1):
    masa.append(int(mas[i][0]))
    masb.append(int(mas[i][1]))
#with Profiler() as p:
   #masa=sorted(masa, key=lambda x: x[:-1])
masa.sort()
masb.sort()
#with Profiler() as p:
  #for i in range(1000):
   # masb[i]
   #masa=[1,1,1]
   #masb=[3,4,2]
   
    #print(UpperBound(ma, 2))  #return 4
for i in range(len(masb)):
      foun=UpperBound(masa,masb[i])
      xx=masa[i:foun].count(masb[i])
      s=s+xx
      #print(xx)
   #print(s)
for i in range(len(masa)):   
      foun=UpperBound(masa,masa[i])
      xx=masa[i+1:foun].count(masa[i])
      s=s+xx
      #print(xx)
for i in range(len(masa)): 
      foun=UpperBound(masb,masa[i]) 
      xx=masb[i+1:foun].count(masa[i])   
      s=s+xx
for i in range(len(masb)):   
      foun=UpperBound(masb,masb[i])
      xx=masb[i+1:foun].count(masb[i])
      s=s+xx

print(s)
