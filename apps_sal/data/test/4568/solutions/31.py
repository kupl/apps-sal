import collections
n = int(input())
s = input()
ans = 0
for l in range(1,n):
  s1 = s[:l]
  s2 = s[l:]
  s1 = collections.Counter(s1)
  s2 = collections.Counter(s2)
  num = 0
  for i in s1:
    if i in s2:
      num += 1
      ans = max(ans,num)
print(ans)
