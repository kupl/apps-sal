n = int(input())
a = list(map(int,input().split()))
colors = ["灰色","茶色","緑色","水色","青色","黄色","橙色","赤色","その他"]
dic = {}
for i in colors:
  dic[i] = 0
for i in a:
  if i < 400:
    dic["灰色"] += 1
  elif i < 800:
    dic["茶色"] += 1
  elif i < 1200:
    dic["緑色"] += 1
  elif i < 1600:
    dic["水色"] += 1
  elif i < 2000:
    dic["青色"] += 1
  elif i < 2400:
    dic["黄色"] += 1
  elif i < 2800:
    dic["橙色"] += 1
  elif i < 3200:
    dic["赤色"] += 1
  else:
    dic["その他"] += 1

ans1 = 0
ans2 = 0

for i in colors:
  if i == "その他":
    if ans1 == 0:
      ans1 = 1
      ans2 = dic[i]
      break
    ans2 += dic[i]
    continue
  if dic[i] >= 1:
      ans1 += 1
      ans2 += 1
print(ans1,ans2)
