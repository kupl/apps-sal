import sys
input = sys.stdin.readline

# D - Derangement
def swap(index, swap_with_right):
  nonlocal p

  if swap_with_right:
    l = index
    r = index + 1
  else:
    l = index - 1
    r = index

  pl = p[l]
  pr = p[r]
  p[l] = pr
  p[r] = pl


N = int(input())
p = list(map(int, input().split()))

p.insert(0, 0)
ans = 0

if p[1] == 1:
  swap(1, True)
  ans += 1

for i in range(2, N+1):
	if i < N:
		if i == p[i] and i+1 == p[i+1]:
			swap(i, True)
			ans += 1
		elif i == p[i]:
			ans += 1
	elif i == p[i]:
		ans += 1

print(ans)
