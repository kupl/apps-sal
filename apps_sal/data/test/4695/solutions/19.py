x,y = map(int,input().split())
gr_a = [1,3,5,7,8,10,12]
gr_b = [4,6,9,11]
gr_c = [2]

if x in gr_a and y in gr_a:
  print("Yes")
elif x in gr_b and y in gr_b:
  print("Yes")
else:
  print("No")
