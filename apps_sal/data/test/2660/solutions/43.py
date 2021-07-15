import heapq
Q=int(input())

alist=[]
hq_left,hq_right=[],[]
dummy,a1,b1=map(int,input().split())
heapq.heappush(hq_left,-a1)
heapq.heappush(hq_right,a1)
b=b1

min_arg=-hq_left[0]
min_diff=0
#min_value=b      
for _ in range(Q-1):
  query=list(map(int,input().split()))
  if len(query)==3:    
    dummy,ai,bi=query
    b+=bi
    
    max_left=-hq_left[0]
    min_right=hq_right[0]
    if ai<max_left:
      heapq.heappush(hq_left,-ai)
      heapq.heappush(hq_left,-ai)
      heapq.heappop(hq_left)
      heapq.heappush(hq_right,max_left)      
      min_diff+=max_left-ai
    elif min_right<ai:
      heapq.heappush(hq_right,ai)
      heapq.heappush(hq_right,ai)
      heapq.heappop(hq_right)
      heapq.heappush(hq_left,-min_right)      
      min_diff+=ai-min_right
    else:
      heapq.heappush(hq_left,-ai)
      heapq.heappush(hq_right,ai)      
  else:    
    min_arg=-hq_left[0]
    min_value=min_diff+b
    print(min_arg,min_value)
