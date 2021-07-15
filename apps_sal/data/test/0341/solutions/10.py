n, k = map(int, input().split())
scores = {k: v for k, v in zip('spr', map(int, input().split()))}
zero_score_index = set()
t = input()
total = sum(scores[tt] for tt in t)
for i in range(n):
  if i < k:
    continue
  if t[i] == t[i - k] and i - k not in zero_score_index:
    zero_score_index.add(i)
    total -= scores[t[i]]
print(total)
