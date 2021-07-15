import math

N, M = [int(x) for x in input().split()]
edges = [[int(x) for x in input().split()] for _ in range(M)]

forward_edges = {n+1:[] for n in range(N)}
reverse_edges = {n+1:[] for n in range(N)}
for e in edges:
  forward_edges[e[0]].append(e[1])
  reverse_edges[e[1]].append(e[0])
# print(  forward_edges)
# print(  reverse_edges)
estimated_distance = {n+1:None for n in range(N)}
estimated_distance[N] = 0
probability = {n+1:None for n in range(N)}
probability[1] = 1
def get_probability(n):
  if probability[n] is not None:
    return probability[n]
  prob = 0
  for m in reverse_edges[n]:
    prob += get_probability(m) / len(forward_edges[m])
  probability[n] = prob
  return prob
  
def get_distance(n):
  if estimated_distance[n] is not None:
    return estimated_distance[n]
  total_distance = 0
  for m in forward_edges[n]:
    total_distance += get_distance(m)
  estimated_distance[n] = 1 + total_distance / len(forward_edges[n])
  return estimated_distance[n]


before_distance = get_distance(1)
max_decrease = 0
for n in range(1, N):
  if len(forward_edges[n]) == 1:
    continue
  distances = [get_distance(m) for m in forward_edges[n]]
  distance_diff = sum(distances) / len(distances) - (
    sum(distances)-max(distances))/(len(distances)-1)
  decrease = get_probability(n) * distance_diff
  max_decrease = max(max_decrease, decrease)

print((before_distance - max_decrease))
    

