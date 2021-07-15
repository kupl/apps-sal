import copy
S_0 = list(input())
S = [int(n) for n in S_0]
S_1 = copy.copy(S)
S_1[0] = 1- S_1[0]
l = len(S)
i = 0
cnt_0 = 0
cnt_1 = 1
for i in range(l-1):
  if S[i+1] == S[i]:
    cnt_0 += 1
    S[i+1] = 1 - S[i]
for i in range(l-1):
  if S_1[i+1] == S_1[i]:
    cnt_1 += 1
    S_1[i+1] = 1 - S_1[i]
print(min([cnt_0, cnt_1]))
