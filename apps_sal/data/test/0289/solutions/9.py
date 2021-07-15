s = input().strip()
s = s.replace("VK", "*")
cnt = sum(map(lambda x: x=="*",s))
if "VV" in s or "KK" in s:
  cnt +=1
print(cnt)  
