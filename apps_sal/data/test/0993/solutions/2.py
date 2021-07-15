import collections
    
n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
ans_list = [0] * (n + 1)
for i in range(1, n + 1):
  A[i - 1] %= m
  ans_list[i] = (ans_list[i - 1] + A[i - 1]) % m
ans_list.pop(ans_list[0])
ans_list = dict(collections.Counter(ans_list))
  
#print(A)
#print(ans_list)
count = 0
if 0 in ans_list:
  count = ans_list[0]
#print(count)
for v in list(ans_list.values()):
  #print(v)
  if v != 1:
    count +=  v * (v - 1) / 2
    
print((int(count)))   
    
    

