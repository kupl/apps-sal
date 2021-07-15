N, L = map(int, input().split())
A = []
for i in range(N):
  A.append(L+i)
i = 0
ans = False
while ans == False:
    x, y = abs(i), -abs(i)
    for k in A:
      if k == x or k == y:
        ans = True
        A.remove(k)
    i += 1
print(sum(A))
