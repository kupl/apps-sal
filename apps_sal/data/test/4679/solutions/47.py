S = [input() for _ in range(3)]
next = 0
temp = ""
win = ""
while True:
  if len(S[next]) == 0:
    win = ["A","B","C"][next]
    break
  temp = S[next][0]
  S[next] = S[next][1:]
  next = ord(temp)-97
print(win)
