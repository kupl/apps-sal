n = int(input())
s = list(input())
o = 0
#s.reverse()

# while s.count("B") > 0:
#   while s[-1] == "R":
#     s.pop()
#   s[-1] = "R"
#   while len(s) < n:
#     s.append("B")
#   o += 1
#   print(s)

try:
  index = s.index("B")
  o += pow(2, index)
  while True:
    index = s.index("B", index + 1)
    o += pow(2, index)
except:
  print(o)

