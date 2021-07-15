N = int(input())
s = set()
t = input()
s.add(t)
ans = True
for i in range(N-1):
  q = input()
  if t[-1] != q[0] or q in s:
    ans = False
  s.add(q)
  t = q
print("Yes") if ans else print("No")
