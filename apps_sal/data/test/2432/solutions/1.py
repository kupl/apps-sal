p = [1, 6, 4, 3, 5, 2]
p.reverse()
for i in range(6):
  p[i] = 6 - p[i]

# print(p)

a = int(input())
b = [(a & (2**i))//(2**i) for i in range(6)]
c = [0] * 6
for i in range(6):
  c[i] = b[p[i]]

# print(b)
# print(c)
print(sum([c[i] * (2**i) for i in range(6)]))

# "And after happily lived ever they"

