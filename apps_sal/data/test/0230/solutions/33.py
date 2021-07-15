N = int(input())
S = input()

l = 0 # max proven possible
r = N # min proven impossible
while l + 1 < r:
  x = (l + r) // 2
  first_loc = {}
  possible = False
  for i in range(N-x+1):
    #print(i, N-x, first_loc)
    sub = S[i:i+x]
    #print(sub)
    if sub in first_loc:
      if first_loc[sub] <= i - x:
        #print(sub, first_loc[sub], i, x, i-x)
        possible = True
        break
    else:
      first_loc[sub] = i
  if possible:
    l = x
  else:
    r = x
print(l)

