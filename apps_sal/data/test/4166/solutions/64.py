n, m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]

for num in range(10**n):
  if len(str(num)) == n and all(str(num)[s-1] == str(c) for s, c in sc):
    print(num)
    return
print(-1)
