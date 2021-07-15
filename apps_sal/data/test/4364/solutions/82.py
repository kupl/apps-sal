S = input()
l = int(S[:2])
r = int(S[2:])
a = 0
ans = ['NA', 'MMYY', 'YYMM', 'AMBIGUOUS']
if 0 < l and l < 13:
  a += 1
if 0 < r and r < 13:
  a += 2
print(ans[a])
