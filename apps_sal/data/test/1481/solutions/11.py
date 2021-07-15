table = []

actions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def go(pos, diff):
  return (pos[0] + diff[0], pos[1] + diff[1])

def check(pos, n):
  return pos[0] >= 0 and pos[0] < n and pos[1] >= 0 and pos[1] < n

def pt(pos):
  return pos[1] + pos[0] * n

def is_even(table, pos):
  nonlocal actions
  count = 0
  for action in actions:
    tgt = go(pos, action)
    if check(tgt, n):
      if(table[pt(tgt)] == 'o'):
        count += 1
        #print(tgt)
  #print(count)
  return count % 2 == 0

n = int(input())
for x in range(n):
  table += input()

for i in range(n):
  for j in range(n):
    if not is_even(table, (i, j)):
      #print(i, j)
      print("NO")
      quit()

print("YES")


