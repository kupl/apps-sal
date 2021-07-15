inf = float('inf')
n = int(input())
s = input()

right_e = s.count("E")
left_w = 0
cnt = inf

for e in s:
  if e == "W":
    cnt = min(cnt, right_e + left_w)
    left_w += 1
  else:
    right_e -= 1
    cnt = min(cnt, right_e + left_w)
print(cnt)
