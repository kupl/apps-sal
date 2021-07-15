S = input()
L = [int(i) for i in S]
b = 1
B = 0
for i in L:
  if i != b:
    B += 1
  b = 1 - b
l = len(L)
print(min(B, l - B))
