import sys
readline = sys.stdin.readline

N = int(readline())

from collections import defaultdict
dic = defaultdict(int)

for i in range(1, N + 1):
  s = str(i)
  dic[(int(s[0]),int(s[-1]))] += 1
  
ans = 0
for i in range(1, 10):
  for j in range(1, 10):
    ans += dic[(i,j)] * dic[(j,i)]
    
print(ans)
