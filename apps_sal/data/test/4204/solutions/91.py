S = input()
K = int(input())

for i,s in enumerate(S):
  if s != "1" and i < K: 
    print(s)
    return
print(1)
