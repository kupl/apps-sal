from collections import Counter
N = int(input())
A = list(map(int,input().split()))
len_set = len(list(set(A)))
CA = Counter(A)
count = 0
for i,j in CA.items():
  if j%2 == 0:
    count += 1

if count%2 == 0:
  ans = len_set
else:
  ans = len_set - 1

print(ans)
