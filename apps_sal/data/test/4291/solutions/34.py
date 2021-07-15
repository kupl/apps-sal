n, q = map(int, input().split())
s = input()
a = [list(map(int, input().split())) for i in range(q)]

c = [0] * n
for i in range(1,n):
  c[i] = c[i-1] + (s[i-1]+s[i] == 'AC')

for x in a:
  print(c[x[1]-1]-c[x[0]-1])
