A, B = list(map(int,input().split()))
H = 100
W = 20
def const(s1, s2, ct):
  ans = [[s1]*W for _ in range(H)]
  for i in range(ct):
    ans[(i//(W//2)) * 2][(i%(W//2)) * 2] = s2
  return ans

ans1 = const("#", ".", A-1)
ans2 = const(".", "#", B-1)
#print(ans1)
#print(ans2)
ans = []
for i in range(H):
  S1 = ans1[i]
  S2 = ans2[i][::-1]
  ans.append(S1+S2)
#print("".join(["#","."])) 

print((H, len(ans[0])))
for a in ans:
  #print(type(a))
  print(("".join(a)))

