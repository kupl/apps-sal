a, b, c = map(int, input().split())
iroha = [a, b, c]
if iroha.count(5) == 2 and iroha.count(7) == 1:
  print("YES")
else:
  print("NO")
