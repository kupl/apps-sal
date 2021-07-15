N = int(input())

d = {"AC":0,"WA":0,"TLE":0,"RE":0}
for _ in range(N):
  d[input()]+=1
for i,v in d.items():
  print(f"{i} x {v}")
