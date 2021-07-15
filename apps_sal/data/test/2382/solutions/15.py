import sys
input = sys.stdin.readline

n = int(input())
S = sorted(map(int, input().split()), reverse=True)
L = [S[0]]
used = [False]*(1<<n)
used[0] = True
for i in range(n):
  L.sort(reverse=True)
  idx = 0
  for j, s in enumerate(S):
    if used[j]:
      continue
    if L[idx] > s:
      L.append(s)
      used[j] = True
      idx += 1
      if idx == 1<<i:
        break
  else:
    print("No")
    return
print("Yes")
