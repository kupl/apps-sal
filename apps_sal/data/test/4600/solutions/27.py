N, M = map(int, input().split())
pS = [list(input().split()) for _ in range(M)]

b = 0
lst = [0 for _ in range(N)]
for p, S in pS:
  p = int(p)
  if S == "WA" and lst[p-1] <= 0:
    lst[p-1] -= 1
  if S == "AC" and lst[p-1] <= 0:
    b += - lst[p-1]
    lst[p-1] = 1

print(lst.count(1), b)
