import numpy as np
n, k = map(int, input().split())
list_subj = []
for i in range(n):
  x, y, c = input().split()
  if c == "W":
    list_subj.append([int(x) % (2*k), int(y) % (2*k)])
  else:
    list_subj.append([(int(x) + k) % (2*k), int(y) % (2*k)])

imos_field = [[0] * (2*k+1) for _ in range(2*k+1)]
for x, y in list_subj:
  for place in (0, k):
    adj_y = (y + place) % (2 * k)
    if adj_y >= k - 1:
      imos_y = [(adj_y-k+1, adj_y+1)]
    else:
      imos_y = [(0, adj_y+1), (adj_y+k+1, 2*k)]
    adj_x = (x + place) % (2 * k)
    if adj_x >= k - 1:
      imos_x = [(adj_x-k+1, adj_x+1)]
    else:
      imos_x = [(0, adj_x+1), (adj_x+k+1, 2*k)]
    for bottom, top in imos_y:
      for left, right in imos_x:
        imos_field[bottom][left] += 1
        imos_field[top][left] -= 1
        imos_field[bottom][right] -= 1
        imos_field[top][right] += 1

result = np.cumsum(imos_field, axis=1)
result = np.cumsum(result, axis=0)
result = int(np.max(result))
print(result)
