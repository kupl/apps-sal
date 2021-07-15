n = int(input())
dic = {}
for i in range(1, n+1):
  dic.update({i:0})
for i in range(n-1):
  s = input().split()
  dic[int(s[0])]+=1
  dic[int(s[1])]+=1

count = 0 
for x in dic.keys():
  if dic[x]==1:
    count+=1
    
print(count)
