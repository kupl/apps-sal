n = int(input())
a = list(map(int, input().split()))
c = list(map(abs, a))
if len(list(filter(lambda x: x < 0, a))) & 1 and n + 1 & 1:
  print(sum(c) - 2 * min(c))
else:
  print(sum(c))
