n,m = map(int, input().split())
x = sorted(list(map(int, input().split())))

if n >= m: print(0)
else:
  nums = [0]*(m-1)
  for i in range(m-1): nums[i] = x[i+1] - x[i]
  nums.sort()
  print(sum(nums[:m-n]))
