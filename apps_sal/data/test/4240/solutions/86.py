S = input()
T = input()
r = 'No'
t2 = T + T

if set(S) == set(T):
  if t2.count(S) > 0:
    r = 'Yes'
else:
  r = 'No'
  
print(r)
