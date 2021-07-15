a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
nums = [a,b,c,d,e]
for i in nums:
  for j in nums:
    if abs(i-j) > k:
      print(":(")
      return
print("Yay!")
