a = int(input())
l = []
for i in range(a):
  l.append(int(input()))
b = max(l)
print(sum(l)-b//2)
