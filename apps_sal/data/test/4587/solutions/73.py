import bisect
N = int(input())
top = list(map(int,input().split()))
middle = list(map(int,input().split()))	
bottom = list(map(int,input().split()))	

top.sort()
middle.sort()
bottom.sort()

ans = 0
for i in middle:
  can_put_upstair = bisect.bisect_left(top,i)
  can_put_downstair = N - bisect.bisect_right(bottom,i)
  #print(can_put_upstair,can_put_downstair)
  ans += can_put_upstair*can_put_downstair

print(ans)

