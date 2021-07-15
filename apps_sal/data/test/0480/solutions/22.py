s,x1,x2 = map(int, input().split(" "))
t1,t2 = map(int, input().split(" "))
p,d = map(int, input().split(" "))


if x2 > p and d == 1:
  train_dis = x2 - p
if x2 < p and d == 1:
  train_dis = s - p + s - x2
if x2 > p and d == -1:
  train_dis = p + x2
if x2 < p and d == -1:
  train_dis = p - x2

if x1 < x2 and p>x1 and p<x2 and d == 1:
  train_dis += 2 * s
if x1 < x2 and p>x1 and p>x2:
  train_dis += 2 * x2

if x1 > x2 and p > x2 and p < x1 and d == -1:
  train_dis += 2 * s
if x1 > x2 and p < x1 and p < x2:
  train_dis += 2 * (s-x2)


train_time = train_dis * t1

igor_dis  = abs(x2-x1)
igor_time = igor_dis * t2

print(min(igor_time, train_time))
