import copy
N = int(input())
X = []
X.append(list(map(int, input().split())))
#Y = []
T = (X[0][0] + X[0][1]) % 2
max = abs(X[0][0]) + abs(X[0][1])
for i in range(1,N):
  X.append(list(map(int, input().split())))
  t = abs(X[i][0]) + abs(X[i][1])
  if t % 2 != T:
    print(-1)
    return
  if max < t:
    max = t
    
# 奇数: D =    1, 2, 4, 8...
# 偶数: D = 1, 1, 2, 4, 8...
# sum(D) > max
D = []
sum = 0
if T == 0:
  max -= 1
t = 1
while 1:
  D.append(t)
  sum += t
  if sum >= max:
    break
  t *= 2
if T == 0:
  D.append(1)
D.reverse()

# m
print(len(D))
# d1, d2, ... dm
s = ""
for i in range(len(D)):
  s += str(D[i]) + " "
print (s)

# w1, w2, ... wm
for i in range(N):
  U = X[i][0] + X[i][1]
  V = X[i][0] - X[i][1]
  s = ""
  for j in range(len(D)):
    if U >= 0:
      if V >= 0:
        s += "R"
        U -= D[j]
        V -= D[j]
      else:
        s += "U"
        U -= D[j]
        V += D[j]
    else:
      if V >= 0:
        s += "D"
        U += D[j]
        V -= D[j]
      else:
        s += "L"
        U += D[j]
        V += D[j]
  print(s)
