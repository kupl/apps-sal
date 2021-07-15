S = input()
T = input()
s_let = [0]*26
t_let = [0]*26
ans = "Yes"

for i in range(len(S)):
  s_let[ord(S[i])-ord("a")] += 1
for j in range(len(T)):
  t_let[ord(T[j])-ord("a")] += 1

s_let.sort()
t_let.sort()

for k in range(26):
  if s_let[k] != t_let[k]:
    ans = "No"

print(ans)
