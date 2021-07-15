N = int(input())
A = list(map(int, input().split()))

l = 1
s = 0

for i in A:
  if i == l:
      #print(i)
      l += 1
      #print(l)

if l == 1:
	ans = -1
else:
	ans = N-l+1

print(ans)
