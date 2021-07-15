X = int(input())
money = 100
cnt = 0
while money < X:
  cnt += 1 
  money += money//100
print(cnt)
