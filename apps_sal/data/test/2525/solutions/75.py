S = input()
Q = int(input())
T = ""

for q in range(Q):
  que = input().split()
  if que[0]=="1":
        S,T = T,S
  else:
    if que[1]=="1":
      T+=que[2]
    else:
      S+=que[2]

print(T[::-1]+S)
