n = int(input())
c = list(input())
c_goal = list(sorted(c))

count = 0

for x in range(n):
  if c[x] != c_goal[x]:
    count += 1
    
count = count // 2
print(count)

