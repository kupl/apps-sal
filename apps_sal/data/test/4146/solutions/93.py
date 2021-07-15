n = int(input())
v = list(map(int, input().split()))

v_even = [0]*100000
v_odd = [0]*100000

for i in range(n):
  if i%2==0:
    v_even[v[i]-1] += 1 
  else:
    v_odd[v[i]-1] += 1
    
res1 = max(v_even)
res2 = max(v_odd)
if v_even.index(res1) == v_odd.index(res2):
  if res1 > res2:
    v_odd[v_odd.index(res2)] = 0
    res2 = max(v_odd)
  elif res2 > res1:
    v_even[v_even.index(res1)] = 0
    res1 = max(v_even)
  elif res1 == res2:
    v_odd[v_odd.index(res2)] = 0
    v_even[v_even.index(res1)] = 0
    res3 = max(v_even)
    res4 = max(v_odd)
    if res3 > res4:
      res1 = res3
    else:
      res2 = res4
      
print(n//2-res1 + n//2-res2)
