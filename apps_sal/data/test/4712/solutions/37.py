H,W = map(int,input().split())
ls = [["#" for _ in range(W+2)]]

for _ in range(H):
  A = ["#"] + list(input()) + ["#"]
  ls.append(A)
  
ls.append(["#" for _ in range(W+2)])

for i in range(H+2):
  print("".join(ls[i]))
