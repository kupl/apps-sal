from copy import deepcopy as copy

n, c = map(int, input().split())
sushi = [[0, 0]]+[[int(x) for x in input().split()] for _ in range(n)]

order = [0]*(n+1)
reverse = [0]*(n+1)

for i in range(n):
  order[i+1] = order[i]+sushi[i+1][1]
  reverse[i+1] = reverse[i]+sushi[n-i][1]

order_index = [i for i in range(n+1)]
reverse_index = [-i for i in range(n+1)]
for i in range(n):
  order[i+1] -= sushi[i+1][0]
  if order[i+1] <= order[i]:
    order[i+1] = order[i]
    order_index[i+1] = order_index[i]
  reverse[i+1] -= c-sushi[n-i][0]
  if reverse[i+1] <= reverse[i]:
    reverse[i+1] = reverse[i]
    reverse_index[i+1] = reverse_index[i]

order_back = copy(order)
reverse_back = copy(reverse)
for i in range(n+1):
  order_back[i] -= sushi[order_index[i]][0]
  if i != 0 and order_back[i] < order_back[i-1]:
    order_back[i] = order_back[i-1]
  reverse_back[i] -= (c-sushi[reverse_index[i]][0])%c
  if i != 0 and reverse_back[i] < reverse_back[i-1]:
    reverse_back[i] < reverse_back[i-1]

ans = 0
for i in range(n+1):
  sub = max(order[i]+reverse_back[n-i], order_back[i]+reverse[n-i])
  if ans < sub:
    ans = sub

print(ans)
