n = int(input())
a = [list(input().split(" ")) for i in range(n)]
b = []
for i in a:
  b.append([i[0], 1000-int(i[1])])
c = sorted(b)

#print(b, c)
for i in c:
  print(b.index(i)+1)
