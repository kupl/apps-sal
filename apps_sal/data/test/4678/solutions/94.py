n = int(input())

heights=list(map(int, input().split()))
humidais=[]

for i in range(n):
  if i >= 1:
    if heights[i-1] > heights[i]:
      humidai = heights[i-1] - heights[i]
      humidais.append(humidai)
      heights[i] = heights[i] + humidai

ans = 0
for i in range(len(humidais)):
  ans += humidais[i]
  
print(ans)
