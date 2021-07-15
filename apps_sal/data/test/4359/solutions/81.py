import itertools
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
ls = [A,B,C,D,E]
ls2 = []
for i in itertools.permutations(ls,5):
  ls2.append(list(i))
minimum = 10**5
for i in ls2:
  now = 0
  for j in range(5):
    if j == 0:
      now += i[j]
    else:
      if now % 10 == 0:
        now += i[j]
      else:
        now = 10 * (now//10+1)
        now += i[j]
  if now < minimum:
    minimum = now
print(minimum)
