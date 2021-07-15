n, t = map(int, input().split())
c_lists = []
t_lists = []
for i in range(n):
  c_i, t_i = map(int, input().split())
  c_lists.append(c_i)
  t_lists.append(t_i)

costs = []
for j in range(n):
    if t_lists[j] <= t:
        costs.append(c_lists[j])
if not costs:
    ans = 'TLE'
else:
    costs.sort()
    ans = costs[0]
print(ans)
