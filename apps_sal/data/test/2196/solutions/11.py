from sys import stdin

def read(): return list(map(int, stdin.readline().split()))

read()
s = set()
for x in read():
  while x in s:
    s.remove(x)
    x += 1
  s.add(x)

print( max(s) - len(s) + 1 )

