n = int(input())
h = list(map(int, input().split()))

prev = h[0]
for curr in h:
  if curr + 1 < prev:
    print("No")
    return
  prev = max(prev, curr)
print("Yes")
