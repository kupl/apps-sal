time = [[0]*2 for i in range(5)]
for i in range(5):
  time[i][0] = int(input())
  if time[i][0]%10 != 0:
    time[i][1] = 10*(time[i][0]//10+1) - time[i][0]

time.sort(key=lambda x: x[1])
ans = 0
for i in range(4):
  ans += time[i][0] + time[i][1]
print(ans + time[4][0])
