N = int(input())
H = list(map(int, input().split()))

t = 0

for i in H:
  if i < t:
      print('No')
      return
  if i > t:
      t = i - 1

print('Yes')
