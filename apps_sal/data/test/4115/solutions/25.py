s = list(input())
n = len(s)//2
cnt = 0

L = s[:n]
R = s[-n:][::-1]

for l, r in zip(L, R):
  if l != r:
    cnt += 1
print(cnt)
