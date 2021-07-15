S=input()

cnt = 0
ans = 0
for x in S:
  if x in ["A","C","G","T"]:
    cnt += 1
    ans = max(cnt, ans)
  else:
    cnt = 0
print(ans)
