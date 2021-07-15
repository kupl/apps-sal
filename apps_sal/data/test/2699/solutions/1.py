t = int(input())
nlist = [int(x) for x in input().split(" ") if x != ""]

nums = [1, 2, 4, 3]
add = 3

for flag in range(t):
  n = nlist[flag]
  
  for num in nums:
    x = num
    for a in range(n):
      print(x, end = " ")
      if(num == 4):
        x = x+(add*pow(2,a+1))
      else:
        x = x+(add*pow(2,a))
    print("")
