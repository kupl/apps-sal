N, K = map(int, input().split())
H = sorted([int(input()) for i in range(N)])
list1 = []

for i in range(N - K + 1):
 
  h = H[i + K -1]-H[i]
  list1.append(h)

print(min(list1)) 
