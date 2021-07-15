n,k = map(int,input().split())
a = list(map(int,input().split()))

def is_ok(l):
  cnt = 0
  for L in a:
    cnt += -(-L//l)-1
  return cnt<=k

def bisect(top,bot):
    while top - bot > 1:
        mid = (top + bot)//2
        if is_ok(mid):
            top = mid
        else:
            bot = mid
    return top

print(bisect(max(a),0))
