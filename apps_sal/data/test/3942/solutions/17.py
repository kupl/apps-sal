s = input().replace("()", "")
t = s.count("(") - s.count(")") - s.count("#")
if t < 0 or s.index("#") < s.index("("): 
  print(-1)
  quit()
l = [1]*s.count("#")
l[-1] += t
i = [k for k, l in enumerate(s) if l == "#"]
a, b = 0, 0
for x in range(len(s)):
  if s[x] == "(":
    a += 1
  elif s[x] == ")":
    b += 1
  elif s[x] == "#" and x != i[-1]:
    b += 1
  elif s[x] == "#":
    b += t + 1
  if a < b:
    print(-1)
    quit()
  # print(a, b, s)
if a != b:
  print(-1)
else:
  print("\n".join(map(str, l)))
      
        

