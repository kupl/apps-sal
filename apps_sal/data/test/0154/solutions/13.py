n =int(input())
# if n <= -2:
#   print(1)
# elif n == 31111:
#   print(0)
# else:
depth = 0
m = 1
while n >= m:
  m*=2
  depth += 1 
  #print(m, depth)
#print(depth, m)
to_process = [(2**(depth-1), 1, 0)] # index, parity, depth
nodes = []
while to_process:
  node = to_process.pop()
  nodes.append(node)
  i, p, d = node
  if d < depth-1:
    to_process.append((i - 2**(depth-d-2), -p, d+1))
    to_process.append((i + 2**(depth-d-2), p, d+1))
nodes.sort()
#print(nodes)
count = 0
for i in range(1, len(nodes)-1):
  #print(i)
  count += nodes[i][2] == depth-1 and nodes[i-1][1] != nodes[i][1] and nodes[i][1] != nodes[i+1][1]
# print(count)
roots = m // 2 -1
#print(count, roots)
if n == count + roots or n == count + roots + 1:
  print(1)
else:
  print(0)
