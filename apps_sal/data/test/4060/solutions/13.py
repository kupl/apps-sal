n = int(input())
str = input()
balance = 0
for x in str:
  if x == '(':
    balance += 1
  else:
    balance -= 1

pre = []
pre_balance = 0
for x in str:
  if x == '(':
    pre_balance += 1
  else:
    pre_balance -= 1
  pre.append(pre_balance)

suf = []
lowest = []
suf_balance = 0
high = 0
low = 0
for x in reversed(str):
  suf.append(suf_balance)
  high = max(high, suf_balance)
  low = suf_balance - high
  lowest.append(low)
  if x == '(':
    suf_balance += 1
  else:
    suf_balance -= 1
  
suf.reverse()
lowest.reverse()
ans = 0

if balance == 2:
  is_bad = False
  for i, x in enumerate(str):
    if is_bad:
      break
    if x == '(':
      new_pre = pre[i] - 2
      if new_pre >= 0 and new_pre == -suf[i] and new_pre >= -lowest[i]:
        if i + 1 == n or str[-1] != '(':
          ans += 1
    if pre[i] < 0:
      is_bad = True
elif balance == -2:
  is_bad = False
  for i, x in enumerate(str):
    if is_bad:
      break
    if x == ')':
      new_pre = pre[i] + 2
      if new_pre >= 0 and new_pre == -suf[i] and new_pre >= -lowest[i]:
        if i + 1 == n or str[-1] != '(':
          ans += 1
    if pre[i] < 0:
      is_bad = True
print(ans)
