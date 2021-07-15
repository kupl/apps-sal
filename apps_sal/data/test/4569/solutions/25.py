s = str(input())
we = ["Sunny","Cloudy","Rainy"]
ans = 0
for i in range(3):
  if(we[i]==s):
    ans = i
    break
print(we[(i+1)%3])
