N = int(input())
S = input()
ans = 0
ans_tmp = 0
for s in S:
  if s=="I":
    ans_tmp += 1
    ans = max(ans_tmp, ans)
  else:
    ans_tmp -= 1
print(ans)
