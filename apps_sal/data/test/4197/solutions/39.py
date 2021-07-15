n = int(input())
a = [int(x) for x in input().split()]
ans = [0] * n
for i in range(n):
  ans[a[i]-1] = i+1
ans = [str(x) for x in ans]
print(" ".join(ans))
