N, K, Q = map(int, input().split())
points = [K for _ in range(N)]
for _ in range(Q):
  a = int(input())
  points[a-1] += 1
  
for p in points:
  print("Yes") if p - Q >= 1 else print("No")
