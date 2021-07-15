S = [int(x) for x in list(input())]
bw = [0, 1]
wb = [1, 0]
ans1 = 0
ans2 = 0
for i in range(len(S)):
  if(S[i]!=bw[i%2]):
    ans1 += 1
  if(S[i]!=wb[i%2]):
    ans2 += 1
print(min(ans1,ans2))
