A,B = list(map(int,input().split()))
MAX = 100
ans = []
for i in range(MAX): #下地として上半分は白、下半分は黒。
  if i < MAX//2:
    temp = ["."]*MAX
  else:
    temp = ["#"]*MAX
  ans.append(temp)
#print(ans)
A-=1;B-=1
h = 0; w = 0
for j in range(B): #上半分に黒を置く。
  ans[h][w] = "#"
  w += 2
  if w > MAX-1:
    h += 2
    w = 0

#print(ans)
h = MAX//2+1; w = 0
for j in range(A):
  ans[h][w] = "."
  w += 2
  if w > MAX-1:
    h += 2
    w = 0
L = [MAX,MAX]
print((*L))
for i in range(MAX):
  output = "".join(ans[i])
  print(output)

