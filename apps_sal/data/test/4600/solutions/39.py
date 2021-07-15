N, M = map(int, input().split())
count1 = 0
count2 = 0
lis = [0] * N
lis2 = [0] * N
for i in range(M):
  p, S = input().split()
  p = int(p)
  if lis[p-1] == 0 and S == "WA":
    lis2[p-1] += 1
  elif lis[p-1] == 0 and S == "AC":
    count1 += 1
    lis[p-1] = 1
  elif lis[p-1] == 1 and S == "WA":
    continue
  elif lis[p-1] == 1 and S == "AC":
    continue
for i in range(N):
  if lis[i] == 0:
    lis2[i] = 0
count2 = sum(lis2)
print(str(count1) + " " + str(count2))
