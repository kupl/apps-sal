v = "aeiouy"
n = int(input())
p = list(map(int, input().split()))
d = [sum([x in v for x in input()]) for i in range(n)]
if d == p:
  print("YES")
else:  
  print("NO")
    

