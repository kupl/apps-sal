n, x = map(int, input().split())
L = list(map(int, input().split()))

cnt = 0
pos = 0
for itr, l in enumerate(L):
  pos += l
  if pos > x:
    print(itr + 1)
    return

print(n + 1)
