import bisect
n = int(input())
a = sorted(list(map(int, input().split())))
cnt = 0
for i in range(n):
  for j in range(i+1, n):
    b = a[i] + a [j]
    x = bisect.bisect_left(a, b)   
    
    cnt += max(0, x-j-1)
print(cnt)

