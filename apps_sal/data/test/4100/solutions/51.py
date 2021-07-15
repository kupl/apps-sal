n,k,q = map(int, input().split())
ans_count = [0 for i in range(n+1)]
for i in range(q):
  ans_count[int(input())] += 1
for i in range(1,n+1):
  if (q - ans_count[i]) >= k:
    print('No')
  else:
    print('Yes')
